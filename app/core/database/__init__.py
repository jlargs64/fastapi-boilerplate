from sqlalchemy.ext.declarative import declarative_base
from .factory import DatabaseFactory
from ..config import get_settings

settings = get_settings()
db_adapter = DatabaseFactory.create_adapter(settings.DATABASE_URL)

Base = declarative_base()


def get_db():
    db = db_adapter.create_session()
    try:
        yield db
    finally:
        db.close()
