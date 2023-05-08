import psycopg2
import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()


def sql_read_users(query, parameters=[]):
    """Function works"""
    # connection
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.close()
    return results


def sql_write_users(query, parameters=[]):
    """Function works"""
    # connection
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()


def add_user(name, email, pw):
    """Function works"""
    hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    sql_write_users("INSERT INTO users(name, email, password_hash) VALUES (%s, %s, %s);",
                    [name, email, hashed_pw])


def user_convert_to_dictionary(user):
    """Function works"""
    return {"id": str(user[0]), "name": user[1], "email": user[2], "password_hash": user[3]}


def get_user(id):
    """Function works"""
    user = sql_read_users("SELECT * FROM users WHERE id=%s;", [id])[0]
    return user_convert_to_dictionary(user)


def update_user(id, name, email):
    """Function works"""
    sql_write_users("UPDATE users SET name=%s, email=%s WHERE id=%s",
                    [name, email, id])


def update_user_password(id, pw):
    """Function works"""
    hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    sql_write_users("UPDATE users SET password_hash=%s WHERE id=%s",
                    [hashed_pw, id])


def delete_user_account(id):
    """Function works"""
    sql_write_users("DELETE FROM users WHERE id=%s;", [id])


def get_user_if_valid(email, password):
    # get user from database via email
    result = sql_read_users("SELECT * FROM users WHERE email=%s;", [email])
    # if user exists check password
    if len(result) == 0:
        # No users with this email address found in database
        return None
    else:
        # User found in database > Check Password:
        user = user_convert_to_dictionary(result[0])
        is_valid = bcrypt.checkpw(
            password.encode(), user["password_hash"].encode())
        if is_valid:
            return user
        else:
            return None
