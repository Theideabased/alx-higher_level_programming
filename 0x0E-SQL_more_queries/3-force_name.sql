-- creating a table where name cannot be null
CREATE TABLE IF NOT EXISTS force_name;
INSERT INTO force_name
(id INT, name VARCHAR(256) NOT NULL)
