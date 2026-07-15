import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6002",
        database="library_db"
    )

    cursor = connection.cursor()

    book_id = int(input("Enter Book ID to update: "))

    # Check if the book exists
    cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
    book = cursor.fetchone()

    if book:
        print("\nCurrent Book Details")
        print("-" * 35)
        print(f"Book ID  : {book[0]}")
        print(f"Title    : {book[1]}")
        print(f"Author   : {book[2]}")
        print(f"Category : {book[3]}")
        print(f"Quantity : {book[4]}")

        new_quantity = int(input("\nEnter New Quantity: "))

        cursor.execute(
            "UPDATE books SET quantity = %s WHERE book_id = %s",
            (new_quantity, book_id)
        )

        connection.commit()

        print("\n✅ Book quantity updated successfully!")

    else:
        print("\n❌ Book not found.")

    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"❌ Database Error: {err}")

except ValueError:
    print("❌ Please enter valid numeric values.")