import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6002",
        database="library_db"
    )

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
    connection.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")