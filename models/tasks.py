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


def task_convert_to_dictionary(task):
    """Function Works!"""
    return {"id": str(task[0]), "user_id": str(task[1]), "item": task[2], "is_done": task[3]}


def get_task_item(id):
    """Function Works!"""
    item = sql_read_tasks("SELECT * FROM tasks WHERE id=%s;", [id])[0]
    return task_convert_to_dictionary(item)


def get_all_tasks_items(user_id):
    """Function Works!"""
    items = sql_read_tasks(
        "SELECT * FROM tasks WHERE user_id=%s ORDER BY item ASC;", [user_id])
    return [task_convert_to_dictionary(item) for item in items]


def update_task_item(id, item, is_done):
    """Function Works!"""
    sql_write_tasks(
        "UPDATE tasks SET item=%s, is_done=%s WHERE id=%s", [item, is_done, id])


def delete_task_item(id):
    """Function Works!"""
    sql_write_tasks("DELETE FROM tasks WHERE id=%s;", [id])


def delete_all_task_items(user_id):
    sql_write_tasks("DELETE FROM tasks WHERE user_id=%s", [user_id])
