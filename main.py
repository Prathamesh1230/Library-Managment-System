from library_controller import LibraryController
from admin_controller import AdminController

def main():
    print("Welcome to Library Management System")
    library_controller = LibraryController()
    admin_controller = AdminController()

    while True:
        print("\n1. User Portal")
        print("2. Admin Portal")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library_controller.user_menu()
        elif choice == '2':
            admin_controller.admin_menu()
        elif choice == '3':
            print("Thank you for visiting the library!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
