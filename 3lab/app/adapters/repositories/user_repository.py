from app.application.ports.user_port import UserPort
from app.domain.models.user import User

class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_all_users(self):
        return self.users

class InMemoryUserRepository(UserPort):
    def __init__(self):
        self.users: dict[str, User] = {}

    def get_user_by_email(self, email: str) -> User | None:
        return self.users.get(email)

    def create_user(self, name: str, email: str) -> User:
        user = User(name, email)
        self.users[email] = user
        return user
