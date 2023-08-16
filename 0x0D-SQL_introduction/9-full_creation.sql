-- this will creaye a table and the attribute with rows of the attribute
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table
(id, name, score)
VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
