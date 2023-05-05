DROP TABLE IF EXISTS mytable;
CREATE TABLE mytable(
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL,
    is_done BOOLEAN NOT NULL,
    email TEXT NOT NULL
);
INSERT INTO mytable(task, is_done, email)
VALUES('groceries', FALSE, 'test@example.com');
INSERT INTO mytable(task, is_done, email)
VALUES('laundry', TRUE, 'test2@example.com');
INSERT INTO mytable(task, is_done, email)
VALUES('walk the dog', FALSE, 'test@example.com');
INSERT INTO mytable(task, is_done, email)
VALUES('buy gifts', FALSE, 'test3@example.com');
SELECT *
FROM mytable;