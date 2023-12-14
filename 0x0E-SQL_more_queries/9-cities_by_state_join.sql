-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE states.id=state_id
ORDER BY cities.id

/*
-- Assuming the database name is passed as an argument, use the specified database
USE hbtn_0d_usa;

-- List all cities with their corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
*/
