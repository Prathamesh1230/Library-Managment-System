from database import Database
from helpers import input_positive_int

class AdminService:
    def __init__(self):
        self.db = Database()

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        new_book = {
            "id": self.db.get_next_book_id(),
            "title": title,
            "author": author,
            "borrowed": False
        }
        self.db.books.append(new_book)
        print("Book added successfully!")

    def remove_book(self):
        self.view_all_books()
        book_id = input_positive_int("Enter Book ID to remove: ")

        for book in self.db.books:
            if book['id'] == book_id:
                self.db.books.remove(book)
                print("Book removed successfully!")
                return
        print("Book ID not found.")

    def view_all_books(self):
        print("\n--- All Books ---")
        for book in self.db.books:
            status = "Borrowed" if book['borrowed'] else "Available"
            print(f"{book['id']} - {book['title']} by {book['author']} ({status})")

    def view_borrowed_books(self):
        print("\n--- Borrowed Books ---")
        for record in self.db.borrowed_books:
            print(f"User: {record['user']} | Book ID: {record['book_id']}")
