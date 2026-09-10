import mysql.connector

from db_connect import get_connection

connection = get_connection()

if connection:
    try:
        cursor = connection.cursor()

        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        category = input("Enter Category: ")
        quantity = int(input("Enter Quantity: "))

        query = """
        INSERT INTO books
        (book_id, title, author, category, quantity)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (book_id, title, author, category, quantity)

        cursor.execute(query, values)
        connection.commit()

        print("\n✅ Book added successfully!")

        cursor.close()

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")

    except ValueError:
        print("❌ Please enter valid numeric values.")

    finally:
        connection.close()
