# Python Generators – Streaming SQL Rows One by One

## 📌 Project Overview

This project demonstrates how to use **Python generators** to stream data from a MySQL database **one row at a time**, efficiently. It is part of the ALX Backend specialization.

---

## ✅ Objectives

- Connect to a MySQL server and create a database `ALX_prodev`.
- Create a table `user_data` with the following fields:
  - `user_id` (UUID, Primary Key)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Load sample data from `user_data.csv` into the table.
- Use a Python generator to stream each row of data one-by-one.

---

## 🛠️ Files

- `seed.py`: Contains all database logic including:
  - Connecting to MySQL
  - Creating database/table
  - Inserting CSV data
  - Streaming rows with a generator
- `0-main.py`: Test file to demonstrate the workflow.
- `user_data.csv`: CSV file containing sample user data.
- `README.md`: Project documentation.

---

## 🔧 How to Run

1. Make sure MySQL is installed and running.
2. Install required Python package:
   ```bash
   pip install mysql-connector-python
Update MySQL credentials in seed.py (user, password).

Place user_data.csv in the same folder.

Run:

bash
Copy
Edit
./0-main.py
🧠 Generator Function
The generator stream_users(connection) yields one row at a time from the user_data table:

python
Copy
Edit
for user in seed.stream_users(connection):
    print(user)
This makes processing large datasets more memory-efficient.

📋 Sample Output
css
Copy
Edit
connection successful
Table user_data created successfully
Database ALX_prodev is present
[('uuid', 'name', 'email', age), ...]
📌 Requirements
Python 3.6+

MySQL server

mysql-connector-python library

👩🏽‍💻 Author
mary Thuo
