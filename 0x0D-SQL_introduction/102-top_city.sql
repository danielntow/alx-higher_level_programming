-- mysql
USE hbtn_0c_0;
SELECT city,
AVG((value - 32) * 5/9) AS average_temperature
FROM temperatures WHERE (month = 7 OR month = 8)
GROUP BY city
ORDER BY average_temperature DESC LIMIT 3;
