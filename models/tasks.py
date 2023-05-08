import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def sql_read_tasks(query, parameters=[]):

    # connection
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.close()
    return results


def sql_write_tasks(query, parameters=[]):
    """Function Works!"""
    # connection
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()


def add_task_item(user_id, item, is_done):
    """Function Works!"""
    sql_write_tasks("INSERT INTO tasks(user_id, item, is_done) VALUES (%s, %s, %s);",
                    [user_id, item, is_done])
