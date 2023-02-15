/* this will creates the database hbtn_0d_usa
and the table states (in the database hbtn_0d_usa) on your MySQL server */
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--which database to use
USE hbtn_0d_usa;
--create the table states in my already created database
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name(VARCHAR 256) NOT NULL, PRIMARY KEY(id));
