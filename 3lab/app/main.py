from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.adapters.repositories.user_repository import InMemoryUserRepository
from app.adapters.repositories.book_repository import InMemoryBookRepository
from app.adapters.api.routes import get_router  # Імпортуємо функцію

user_repo = InMemoryUserRepository()
book_repo = InMemoryBookRepository()

app = FastAPI()

# Реєструємо роутер з існуючими репозиторіями
app.include_router(get_router(user_repo, book_repo))

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    users_html = ""
    for user in user_repo.users.values():
        books = "<br>".join([f"{book.title} by {book.author}" for book in user.ordered_books])
        users_html += f"""
        <tr>
            <td>{user.name}</td>
            <td>{user.email}</td>
            <td>{books or '-'}</td>
        </tr>
        """

    books_html = ""
    for book in book_repo.books.values():
        books_html += f"""
        <tr>
            <td>{book.title}</td>
            <td>{book.author}</td>
        </tr>
        """

    html_content = f"""
    <html>
    <head>
        <title>Бібліотечний сервіс</title>
        <style>
            body {{ background-color: #121212; color: #fff; font-family: sans-serif; padding: 20px; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 30px; }}
            th, td {{ border: 1px solid #555; padding: 8px; text-align: left; }}
            th {{ background-color: #333; }}
        </style>
    </head>
    <body>
        <h1>Користувачі</h1>
        <table>
            <tr><th>Ім’я</th><th>Email</th><th>Замовлені книги</th></tr>
            {users_html}
        </table>

        <h1>Книги</h1>
        <table>
            <tr><th>Назва</th><th>Автор</th></tr>
            {books_html}
        </table>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
