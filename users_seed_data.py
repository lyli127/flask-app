# DROP TABLE IF EXISTS users;
# CREATE TABLE users(
#     id SERIAL PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     password_hash TEXT NOT NULL
# );
# INSERT INTO users(email, password_hash)
# VALUES('Test1', 'test@example.com', 'password123');
# INSERT INTO users(email, password_hash)
# VALUES('Test2', 'test2@example.com', 'password123');
# INSERT INTO users(email, password_hash)
# VALUES('Test3', 'test3@example.com', 'password123');

import psycopg2
import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()

# connect to database
connection = psycopg2.connect(os.getenv("DATABASE_URL"))

# create object to execute SQL commands
cursor = connection.cursor()


def delete_table():
    # Run DROP TABLE sql
    cursor.execute("DROP TABLE IF EXISTS users;")


def create_table():
    # Run DROP TABLE sql
    # delete_table()

    # create users table
    cursor.execute(
        """CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL);""")


def add_data():
    rows = [
        ['Test1', 'test1@example.com', 'password1'],
        ['Test2', 'test2@example.com', 'password2'],
        ['Test3', 'test3@example.com', 'password3'],
        ['Test4', 'test4@example.com', 'password4'],
        ['Test5', 'test5@example.com', 'password5'],
    ]
    # Loop through data
    for row in rows:
        # Get Data
        name = row[0]
        email = row[1]
        # hash password
        pw = row[2]
        pw.encode()
        hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        # INSERT sql...
        cursor.execute("INSERT INTO users(name, email, password_hash) VALUES (%s, %s, %s);",
                       [name, email, hashed_pw])


delete_table()
create_table()
add_data()

connection.commit()
connection.close()
