-- Create a table named unique_id
-- If the table already exists, this statement won't cause an error
CREATE TABLE IF NOT EXISTS unique_id (
    -- id column with integer data type, default value 1, and must be unique
    id INT DEFAULT 1 UNIQUE,

    -- name column with variable character data type and maximum length of 256 characters
    name VARCHAR(256)
);
