-- Check if the force_name table already exists
USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
);
