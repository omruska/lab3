from app.domain.models.book import Book
from typing import List

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.ordered_books: List[Book] = []
