from abc import ABC, abstractmethod
from app.domain.models.user import User

class UserPort(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create_user(self, name: str, email: str) -> User:
        pass
