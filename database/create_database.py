import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6002"
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")

    print("✅ Database created successfully!")

    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")