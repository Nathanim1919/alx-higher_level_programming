--  a script that creates the database hbtn_0d_usa
--  create table cities

CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	'id' INT UNIQUE AUTO_INCREMENT NOT NULL,
	PRIMARY KEY (id),
	'state_id' INT NOT NULL,
        FOREIGN KEY (state_id) REFERENCES states(id),
	'name' VARCHAR(256)
);
