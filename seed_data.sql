DROP TABLE IF EXISTS mytable;

CREATE TABLE mytable(id SERIAL PRIMARY KEY, item TEXT);
INSERT INTO mytable(item) VALUES('groceries');
INSERT INTO mytable(item) VALUES('laundry');
INSERT INTO mytable(item) VALUES('walk the dog');
INSERT INTO mytable(item) VALUES('buy gifts');

SELECT * FROM mytable;