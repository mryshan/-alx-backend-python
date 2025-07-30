#!/usr/bin/python3
import mysql.connector
import csv
import uuid


def connect_db():
    """
    Connects to MySQL server (without selecting a DB).
    """
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password"
    )


def create_database(connection):
    """
    Creates ALX_prodev database if it doesn't exist.
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()


def connect_to_prodev():
    """
    Connects to the ALX_prodev database.
    """
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="ALX_prodev"
    )


def create_table(connection):
    """
    Creates the user_data table if it does not exist.
    """
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        )
    """)
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()


def insert_data(connection, csv_file):
    """
    Inserts data from a CSV file into user_data table if email not already exists.
    """
    cursor = connection.cursor()
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("SELECT COUNT(*) FROM user_data WHERE email = %s", (row['email'],))
            if cursor.fetchone()[0] == 0:
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()


def stream_users(connection):
    """
    Generator that yields one user record at a time from the user_data table.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()
