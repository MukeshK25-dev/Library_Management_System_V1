import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6002",
        database="library_db"
    )

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
    connection.close()

except mysql.connector.Error as err:
    print(f"❌ Database Error: {err}")

except ValueError:
    print("❌ Please enter a valid Book ID.")