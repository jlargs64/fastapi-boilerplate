from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import DatabaseAdapter


class PostgresAdapter(DatabaseAdapter):
    def __init__(self, db_url: str):
        self.db_url = db_url

    def get_db_url(self) -> str:
        return self.db_url

    def get_engine_kwargs(self) -> dict:
        return {}

    def create_session(self):
        engine = create_engine(self.get_db_url(), **self.get_engine_kwargs())
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return SessionLocal()
