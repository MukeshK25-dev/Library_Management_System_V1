import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Database credentials — loaded from environment, never hardcoded.
# Copy .env.example to .env and fill in your real values.
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE", "library_db")

if not DB_PASSWORD:
    raise RuntimeError(
        "DB_PASSWORD is not set. Create a .env file with DB_PASSWORD=<your-password> "
        "(see .env.example)."
    )


def get_connection(with_database=True):
    """
    Creates and returns a connection to the MySQL server.

    with_database=False connects to the server without selecting a
    database — used by create_database.py, which needs to run
    CREATE DATABASE before library_db exists.
    """

    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE if with_database else None,
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
