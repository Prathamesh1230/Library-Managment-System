from library_manager import LibraryManager

manager = LibraryManager()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        manager.add_book(book_id, title, author)
    elif choice == '2':
        manager.list_books()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")
