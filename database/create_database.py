from db_connect import get_connection

connection = get_connection(with_database=False)

if connection:
    try:
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")

        print("✅ Database created successfully!")

        cursor.close()

    except Exception as err:
        print(f"❌ Error: {err}")

    finally:
        connection.close()
