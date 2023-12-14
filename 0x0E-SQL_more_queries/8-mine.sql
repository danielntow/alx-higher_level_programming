-- Assuming the database name is passed as an argument, use the specified database
USE hbtn_0d_usa;

-- Find the id of California in the states table
SET @california_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1);

-- List all the cities of California, sorted in ascending order by cities.id
SELECT cities.id, cities.name
FROM cities
WHERE state_id = @california_id
ORDER BY cities.id ASC;
