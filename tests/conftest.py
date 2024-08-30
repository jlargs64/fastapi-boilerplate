import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import Base, get_db
from app.core.config import Settings
from app.core.database.factory import DatabaseFactory


def get_test_settings():
    return Settings(DATABASE_URL="sqlite:///./test.db", DATABASE_ECHO=False)


@pytest.fixture(scope="session")
def test_db_adapter():
    settings = get_test_settings()
    adapter = DatabaseFactory.create_adapter(settings.DATABASE_URL)
    engine = adapter.create_session().get_bind()
    Base.metadata.create_all(bind=engine)
    yield adapter
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db(test_db_adapter):
    db = test_db_adapter.create_session()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.rollback()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]
