from db_connect import get_connection

connection = get_connection()

if connection:
    try:
        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            book_id INT PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
            category VARCHAR(50),
            quantity INT
        )
        """

        cursor.execute(create_table_query)

        print("✅ Table created successfully!")

        cursor.close()

    except Exception as err:
        print(f"❌ Error: {err}")

    finally:
        connection.close()
