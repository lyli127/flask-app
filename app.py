from flask import Flask, render_template, request, redirect, session
import os
import psycopg2
import requests
from models import tasks, users
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    # connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable;")
    results = cursor.fetchall()
    connection.close()
    # return f"{results[0]}"
    return render_template("base.html")


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
