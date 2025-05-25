from typing import List
from uuid import UUID
from app.domain.models.order import Order
from app.application.ports.order_port import OrderRepositoryPort

class OrderRepository:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_all_orders(self):
        return self.orders

class InMemoryOrderRepository(OrderRepositoryPort):
    def __init__(self):
        self.orders: List[Order] = []

    def save(self, order: Order):
        self.orders.append(order)

    def get_by_user(self, user_id: UUID) -> List[Order]:
        return [order for order in self.orders if order.user_id == user_id]
