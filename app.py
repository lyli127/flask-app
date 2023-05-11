from flask import Flask, render_template, request, redirect, session
import os
import psycopg2
from models import tasks, users
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


@app.route('/')
def index():
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/signup')
    else:
        return redirect('/tasks/all')


@app.route('/signup')
def signup_form():
    return render_template("signup.html")


@app.route('/api/signup', methods=['POST'])
def signup():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    plain_text_password = request.form.get('password')
    # create user
    users.add_user(name, email, plain_text_password)
    # Call validate_password function
    valid_user = users.get_user_if_valid(email, plain_text_password)
    if valid_user:
        # set session and redirect
        session['user_id'] = valid_user['id']
        print(valid_user)
        return redirect("/task/add")
    else:
        # password was invalid, redirect to login page
        return redirect("/login")

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_validation():
    # Get form data
    email = request.form.get('email')
    plain_text_password = request.form.get('password')
    # Call validate_password function
    valid_user = users.get_user_if_valid(email, plain_text_password)
    if valid_user:
        # set session and redirect
        session['user_id'] = valid_user['id']
        print(valid_user)
        return redirect("/")
    else:
        # password was invalid, redirect to login page
        print("No valid user", valid_user)
        return redirect("/login")
@app.route("/logout")
def logout():
    # cookie still exists, but the value of session is set to null
    session["user_id"] = None
    # session.clear() #removes the cookie entirely
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
