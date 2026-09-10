from db_connect import get_connection

connection = get_connection()

if connection:
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()

        if books:
            print("\n========== BOOK LIST ==========")

            for book in books:
                print("-" * 35)
                print(f"Book ID  : {book[0]}")
                print(f"Title    : {book[1]}")
                print(f"Author   : {book[2]}")
                print(f"Category : {book[3]}")
                print(f"Quantity : {book[4]}")

            print("-" * 35)

        else:
            print("No books found.")

        cursor.close()

    except Exception as err:
        print(f"❌ Error: {err}")

    finally:
        connection.close()
