class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.books = [
            {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "borrowed": False},
            {"id": 2, "title": "1984", "author": "George Orwell", "borrowed": False},
            {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "borrowed": False},
        ]
        self.borrowed_books = []

    def get_next_book_id(self):
        if self.books:
            return max(book['id'] for book in self.books) + 1
        else:
            return 1
