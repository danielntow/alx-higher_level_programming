-- mysql
USE hbtn_0c_0;
SELECT state, MAX(value) as temp
FROM temperatures
GROUP BY state
ORDER BY state
