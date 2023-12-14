-- Create the database hbtn_0d_usa
-- If the database already exists, this statement won't cause an error
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the cities table
-- If the table already exists, this statement won't cause an error
CREATE TABLE IF NOT EXISTS cities (
    -- id column with integer data type, unique, auto-generated, not null, and is the primary key
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,

    -- state_id column with integer data type, not null, and a FOREIGN KEY that references the id of the states table
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),

    -- name column with variable character data type and maximum length of 256 characters, not null
    name VARCHAR(256) NOT NULL
);
