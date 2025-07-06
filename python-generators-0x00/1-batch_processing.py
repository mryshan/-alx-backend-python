#!/usr/bin/python3
import mysql.connector


def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from user_data table.
    Each batch is a list of dictionaries.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FOREVERshan",
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch  # yield remaining records

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Processes each batch and prints users over age 25.
    """
    for batch in stream_users_in_batches(batch_size):         # 1st loop
        for user in (u for u in batch if u["age"] > 25):      # 2nd loop (generator expression)
            print(user)                                       # yield could also be used here if needed
