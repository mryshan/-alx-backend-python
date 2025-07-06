#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev


def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age
    cursor.close()
    connection.close()


def compute_average_age():
    """
    Calculates the average age of users using a generator, memory-efficiently.
    """
    total = 0
    count = 0
    for age in stream_user_ages():  # Loop 1
        total += age
        count += 1
    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")


if __name__ == "__main__":
    compute_average_age()
