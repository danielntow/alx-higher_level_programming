-- Create a table named id_not_null
-- If the table already exists, this statement won't cause an error
CREATE TABLE IF NOT EXISTS id_not_null (
    -- id column with integer data type and default value 1
    id INT DEFAULT 1,

    -- name column with variable character data type and maximum length of 256 characters
    name VARCHAR(256)
);
