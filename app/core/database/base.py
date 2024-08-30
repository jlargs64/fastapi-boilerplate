from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class DatabaseAdapter(ABC):
    @abstractmethod
    def get_db_url(self) -> str:
        pass

    @abstractmethod
    def get_engine_kwargs(self) -> dict:
        pass

    @abstractmethod
    def create_session(self) -> Session:
        pass
