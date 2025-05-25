from uuid import UUID
from app.domain.models.order import Order
from app.application.ports.order_port import OrderRepositoryPort

class OrderService:
    def __init__(self, order_repo: OrderRepositoryPort):
        self.order_repo = order_repo

    def place_order(self, user_id: UUID, book_id: UUID) -> Order:
        order = Order(user_id, book_id)
        self.order_repo.save(order)
        return order
