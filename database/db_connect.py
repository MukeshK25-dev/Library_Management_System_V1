import mysql.connector


def get_connection():
    """
    Creates and returns a connection to the MySQL Server.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6002"
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Server Successfully!")
            return connection

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None


if __name__ == "__main__":
    conn = get_connection()

    if conn:
        conn.close()
        print("Connection Closed.")