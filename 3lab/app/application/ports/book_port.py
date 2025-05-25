from abc import ABC, abstractmethod
from app.domain.models.book import Book

class BookPort(ABC):
    @abstractmethod
    def get_book_by_title(self, title: str) -> Book | None:
        pass

    @abstractmethod
    def create_book(self, title: str, author: str) -> Book:
        pass
