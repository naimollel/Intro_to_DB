#!/usr/bin/python3
"""
Script to create a MySQL database named 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (edit user & password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        # Properly close connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Uncomment if you want confirmation of close:
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
