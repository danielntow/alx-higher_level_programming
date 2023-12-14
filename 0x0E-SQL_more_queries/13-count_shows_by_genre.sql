-- Switch to the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select the genre name from tv_genres and count the number of shows linked to each genre
-- Use an INNER JOIN to include only genres with linked shows
-- Group the results by genre name
-- Order the results in descending order by the number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
