from app.application.ports.book_port import BookPort
from app.domain.models.book import Book

class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books(self):
        return self.books

class InMemoryBookRepository(BookPort):
    def __init__(self):
        self.books: dict[str, Book] = {}

    def get_book_by_title(self, title: str) -> Book | None:
        return self.books.get(title)

    def create_book(self, title: str, author: str) -> Book:
        book = Book(title, author)
        self.books[title] = book
        return book
