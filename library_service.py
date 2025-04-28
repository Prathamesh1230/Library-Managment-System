from database import Database
from helpers import input_positive_int

class LibraryService:
    def __init__(self):
        self.db = Database()

    def view_available_books(self):
        print("\n--- Available Books ---")
        for book in self.db.books:
            if not book['borrowed']:
                print(f"{book['id']} - {book['title']} by {book['author']}")

    def borrow_book(self):
        self.view_available_books()
        book_id = input_positive_int("Enter Book ID to borrow: ")

        for book in self.db.books:
            if book['id'] == book_id and not book['borrowed']:
                user_name = input("Enter your name: ")
                book['borrowed'] = True
                self.db.borrowed_books.append({
                    "user": user_name,
                    "book_id": book_id
                })
                print("Book borrowed successfully!")
                return

        print("Book not available or invalid ID.")

    def return_book(self):
        user_name = input("Enter your name: ")

        for record in self.db.borrowed_books:
            if record['user'] == user_name:
                book_id = record['book_id']
                for book in self.db.books:
                    if book['id'] == book_id:
                        book['borrowed'] = False
                        break
                self.db.borrowed_books.remove(record)
                print("Book returned successfully!")
                return

        print("No borrowed book record found for this user.")
