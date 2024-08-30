from .base import DatabaseAdapter
from .sqlite_adapter import SQLiteAdapter
from .postgres_adapter import PostgresAdapter


class DatabaseFactory:
    @staticmethod
    def create_adapter(db_url: str) -> DatabaseAdapter:
        if db_url.startswith("sqlite"):
            return SQLiteAdapter(db_url)
        elif db_url.startswith("postgresql"):
            return PostgresAdapter(db_url)
        else:
            raise ValueError(f"Unsupported database type: {db_url}")
