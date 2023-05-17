-- a script that creates the database hbtn_0d_usa
-- table states (in the database hbtn_0d_usa) 

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY (id), name VARCHAR(256));
