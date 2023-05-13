# README

# To-Do List App

[**_You can access the app via this link_**](https://project2-ukq4.onrender.com/)

This is the second project out 4 of for General Assembly Software Engineering Intensive Course.
<br/>
<br/>

---

## Technology used:

- HTML
- CSS
- Bootstrap
- Jinja
- Python

## Overall Approach

Tarefas is a to-do list Flask app. The project started with planning: choosing and defining data models and writing the functions. Part of it was thinking all the different was to access data (CRUD). After this was done I created the database tables, first user then tasks, and populated them with dummy data. From then on I was able to test out the model functions I’ve written.

Once this was done I moved to creating the templates and their respective routes. Lastly, I tried keeping the UI simple but still responsive so I chose to use Bootstrap.

## Instructions for local setup

Clone this repo locally, and then inside a virtual environment:

```bash
(venv) pip install -r requirements.txt

# Ensure that Postgres is running locally
(venv) python users_seed_data.py  # Populate `users` table
(venv) psql tasks_seed_data.sql   # Populate `tasks` table

# Once the dummy data is populated you can run the app localy
(venv) python app.py

# The URL to the local app will be shown in your terminal

```

## Upcoming features

- Mark task as done
- Delete account
- Hide/show done tasks
- Task due date
- Add labels/tags
