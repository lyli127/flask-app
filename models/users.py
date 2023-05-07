import psycopg2
import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()


def sql_read_users(query, parameters):
    # connection
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.close()
    return results


def sql_write_users(query, parameters=[]):
    # connection
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()


def add_user(name, email, pw):
    pw.encode()
    hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    sql_write_users("INSERT INTO users(name, email, password_hash) VALUES (%s, %s, %s);",
                    [name, email, hashed_pw])


def convert_to_dictionary(user):
    return {"id": str(user[0]), "name": user[1], "email": user[2]}


def get_user(id):
    user = sql_read_users("SELECT * FROM users WHERE id=%s;", [id])[0]
    return convert_to_dictionary(user)


def update_user(id, name, email, password):
    sql_write_users("UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s",
                    [name, email, password, id])


def delete_user_account(id):
    sql_write_users("DELETE FROM users WHERE id=%s;", [id])
