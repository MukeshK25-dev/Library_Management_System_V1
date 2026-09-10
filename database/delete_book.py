from db_connect import get_connection

connection = get_connection()

if connection:
    try:
        cursor = connection.cursor()

        book_id = int(input("Enter Book ID to delete: "))

        # Check if the book exists
        cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
        book = cursor.fetchone()

        if book:
            print("\nBook Found")
            print("-" * 35)
            print(f"Book ID  : {book[0]}")
            print(f"Title    : {book[1]}")
            print(f"Author   : {book[2]}")
            print(f"Category : {book[3]}")
            print(f"Quantity : {book[4]}")

            choice = input("\nAre you sure you want to delete this book? (yes/no): ").lower()

            if choice == "yes":
                cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
                connection.commit()
                print("\n✅ Book deleted successfully!")
            else:
                print("\nDeletion cancelled.")

        else:
            print("\n❌ Book not found.")

        cursor.close()

    except ValueError:
        print("❌ Please enter a valid Book ID.")

    except Exception as err:
        print(f"❌ Database Error: {err}")

    finally:
        connection.close()
