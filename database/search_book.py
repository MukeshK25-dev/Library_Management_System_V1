from db_connect import get_connection

connection = get_connection()

if connection:
    try:
        cursor = connection.cursor()

        book_id = int(input("Enter Book ID to search: "))

        query = "SELECT * FROM books WHERE book_id = %s"

        cursor.execute(query, (book_id,))

        book = cursor.fetchone()

        if book:
            print("\n📖 Book Found!")
            print("-" * 35)
            print(f"Book ID  : {book[0]}")
            print(f"Title    : {book[1]}")
            print(f"Author   : {book[2]}")
            print(f"Category : {book[3]}")
            print(f"Quantity : {book[4]}")
        else:
            print("\n❌ Book not found.")

        cursor.close()

    except ValueError:
        print("❌ Please enter a valid Book ID.")

    except Exception as err:
        print(f"❌ Database Error: {err}")

    finally:
        connection.close()
