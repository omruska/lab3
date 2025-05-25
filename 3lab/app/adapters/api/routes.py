from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.adapters.repositories.user_repository import InMemoryUserRepository
from app.adapters.repositories.book_repository import InMemoryBookRepository

def get_router(user_repo: InMemoryUserRepository, book_repo: InMemoryBookRepository) -> APIRouter:
    router = APIRouter()

    class UserRegistrationRequest(BaseModel):
        name: str
        email: str

    class BookOrderRequest(BaseModel):
        user_email: str
        book_title: str
        book_author: str

    @router.post("/register")
    def register_user(request: UserRegistrationRequest):
        if user_repo.get_user_by_email(request.email):
            raise HTTPException(status_code=400, detail="User already exists")
        user_repo.create_user(request.name, request.email)
        return {"message": "User registered successfully"}

    @router.post("/order")
    def order_book(request: BookOrderRequest):
        user = user_repo.get_user_by_email(request.user_email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        book = book_repo.get_book_by_title(request.book_title)
        if not book:
            book = book_repo.create_book(request.book_title, request.book_author)

        user.ordered_books.append(book)
        return {"message": f"Book '{book.title}' ordered by {user.name}"}

    @router.get("/users")
    def get_users():
        return [
            {
                "name": user.name,
                "email": user.email,
                "ordered_books": [
                    {"title": book.title, "author": book.author}
                    for book in user.ordered_books
                ]
            }
            for user in user_repo.users.values()
        ]

    @router.get("/books")
    def get_books():
        return [
            {
                "title": book.title,
                "author": book.author
            }
            for book in book_repo.books.values()
        ]

    return router
