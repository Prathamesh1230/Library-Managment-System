from admin_service import AdminService

class AdminController:
    def __init__(self):
        self.admin_service = AdminService()

    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add New Book")
            print("2. Remove Book")
            print("3. View All Books")
            print("4. View Borrowed Books")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.admin_service.add_book()
            elif choice == '2':
                self.admin_service.remove_book()
            elif choice == '3':
                self.admin_service.view_all_books()
            elif choice == '4':
                self.admin_service.view_borrowed_books()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")
