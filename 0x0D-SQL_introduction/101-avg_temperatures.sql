-- list all
USE hbtn_0c_0;
SELECT city,
AVG((value - 32) * 5/9) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
