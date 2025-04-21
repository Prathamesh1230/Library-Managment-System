from book import Book
from file_helper import save_books, load_books

class LibraryManager:
    def __init__(self):
        self.books = load_books()

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        save_books(self.books)
        print("Book added successfully.")

    def list_books(self):
        if not self.books:
            print("No books found.")
        for book in self.books:
            print(book)
