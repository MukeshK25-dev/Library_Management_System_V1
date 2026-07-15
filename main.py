import os

while True:
    print("\n" + "=" * 45)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        os.system("python database/add_book.py")

    elif choice == "2":
        os.system("python database/view_books.py")

    elif choice == "3":
        os.system("python database/search_book.py")

    elif choice == "4":
        os.system("python database/update_book.py")

    elif choice == "5":
        os.system("python database/delete_book.py")

    elif choice == "6":
        print("\nThank you for using the Library Management System.")
        break

    else:
        print("\n❌ Invalid choice. Please enter a number between 1 and 6.")