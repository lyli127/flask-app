DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    item TEXT NOT NULL,
    is_done BOOLEAN NOT NULL,
    CONSTRAINT foreign_key_user FOREIGN KEY(user_id) REFERENCES users(id)
);
INSERT INTO tasks(user_id, item, is_done)
VALUES(1, 'groceries', FALSE);
INSERT INTO tasks(user_id, item, is_done)
VALUES(2, 'laundry', TRUE);
INSERT INTO tasks(user_id, item, is_done)
VALUES(3, 'walk the dog', FALSE);
INSERT INTO tasks(user_id, item, is_done)
VALUES(4, 'buy gifts', FALSE);
INSERT INTO tasks(user_id, item, is_done)
VALUES(4, 'buy coffee', FALSE);
-- Print Task Table
SELECT *
FROM tasks;
-- Print both tables
SELECT user_id,
    item,
    is_done,
    users.name,
    email
FROM tasks
    LEFT JOIN users ON user_id = users.id;