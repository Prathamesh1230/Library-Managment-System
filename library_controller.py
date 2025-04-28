from library_service import LibraryService

class LibraryController:
    def __init__(self):
        self.library_service = LibraryService()

    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print("1. View Available Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Back")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.library_service.view_available_books()
            elif choice == '2':
                self.library_service.borrow_book()
            elif choice == '3':
                self.library_service.return_book()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again.")
