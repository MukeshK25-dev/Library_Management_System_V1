import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6002",
        database="library_db"
    )

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
    connection.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")