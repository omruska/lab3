from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.models.order import Order

class OrderRepositoryPort(ABC):
    @abstractmethod
    def save(self, order: Order): pass

    @abstractmethod
    def get_by_user(self, user_id: UUID) -> list[Order]: pass
