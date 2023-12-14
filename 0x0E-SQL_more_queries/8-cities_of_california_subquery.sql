--  lists all the cities of California
SELECT id, name
FROM
	(SELECT * FROM cities WHERE state_id =
		(SELECT id FROM states WHERE name = 'California')) AS name

/*
-- Assuming the database name is passed as an argument, use the specified database
USE hbtn_0d_usa;

-- Find the id of California in the states table
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- List all the cities of California, sorted in ascending order by cities.id
SELECT cities.id, cities.name
FROM cities
WHERE state_id = @california_id
ORDER BY cities.id ASC;
*/