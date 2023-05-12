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


@app.route('/login', methods=['GET'])
def login_form():
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


# View Tasks
@app.route('/tasks/all')
def view_all_tasks():
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        return render_template("view_all_tasks.html", items=tasks.get_all_tasks_items(session['user_id']), user=users.get_user(session['user_id']))


# Create Task
@app.route('/task/add')
def add_task_form():
    return render_template("add.html")


@app.route('/api/task/add', methods=["POST"])
def add_task_item():
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        form = request.form
        item = form.get("task_item")
        is_done = False
        user_id = users.get_user(session['user_id'])['id']
        tasks.add_task_item(user_id, item, is_done)
        return redirect('/tasks/all')


# Edit Tasks
@app.route('/task/edit/<id>')
def edit_task_form(id):
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        return render_template("edit.html", item=tasks.get_task_item(id))


@app.route('/api/task/edit/<id>', methods=["POST"])
def edit_task(id):
    form = request.form
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        tasks.update_task_item(id, form.get('item'), False)
        return redirect('/tasks/all')


@app.route('/task/delete/<id>')
def delete_task_form(id):
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        return render_template("delete.html", item=tasks.get_task_item(id))


@app.route('/api/task/delete/<id>', methods=["POST"])
def delete_task(id):
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        tasks.delete_task_item(id)
        return redirect('/tasks/all')


@app.route('/tasks/delete/all')
def delete_all_tasks_form():
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        user_id = users.get_user(session['user_id'])['id']
        return render_template("delete_all.html", item=tasks.get_all_tasks_items(user_id))


@app.route('/api/tasks/delete/all', methods=["POST"])
def delete_all_tasks(user_id):
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        user_id = users.get_user(session['user_id'])['id']
        tasks.delete_all_task_items(user_id)
        return redirect('/tasks/all')


@app.route('/user/edit/<user_id>')
def edit_user_form(user_id):
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        user_id = users.get_user(session['user_id'])['id']
        return render_template("user_profile.html", user=users.get_user(user_id))


@app.route('/api/user/edit/<user_id>', methods=["POST"])
def edit_user(user_id):
    form = request.form
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        user_id = users.get_user(session['user_id'])['id']
        users.update_user(user_id, form.get('name'), form.get('email'))
        return redirect('/')


@app.route('/user/password/<user_id>')
def user_password_form(user_id):
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        user_id = users.get_user(session['user_id'])['id']
        return render_template("update_password.html", user=users.get_user(user_id))


@app.route('/api/user/password/<user_id>', methods=["POST"])
def user_password(user_id):
    form = request.form
    is_authed = session.get('user_id')
    if not is_authed:
        # user is logged out
        return redirect('/login')
    else:
        user_id = users.get_user(session['user_id'])['id']
        users.update_user_password(user_id, form.get('password'))
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", default=5000)))
