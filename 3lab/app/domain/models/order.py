from uuid import UUID, uuid4

class Order:
    def __init__(self, user_id: UUID, book_id: UUID):
        self.id = uuid4()
        self.user_id = user_id
        self.book_id = book_id
