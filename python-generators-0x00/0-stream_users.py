#!/usr/bin/python3
import mysql.connector

def stream_users():
    """
    Generator that yields one row at a time from user_data table as a dictionary.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FOREVERshan",
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
