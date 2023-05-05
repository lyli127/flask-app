# DROP TABLE IF EXISTS users;
# CREATE TABLE users(
#     id SERIAL PRIMARY KEY,
#     email TEXT NOT NULL,
#     password_hash TEXT NOT NULL
# );
# INSERT INTO users(email, password_hash)
# VALUES('test@example.com', 'password123');
# INSERT INTO users(email, password_hash)
# VALUES('test2@example.com', 'password123');
# INSERT INTO users(email, password_hash)
# VALUES('test3@example.com', 'password123');

def delete_table():
    # Run DROP TABLE sql
    pass


def create_table():
    # Run DROP TABLE sql
    pass


def add_data():
    rows = [
        [1, 2, "hashed_pw"],
        [4, 5, "hashed_pw"]
    ]

    for row in rows:
        # hash password
        # INSERT sql...
        pass


delete_table()
create_table()
add_data()
