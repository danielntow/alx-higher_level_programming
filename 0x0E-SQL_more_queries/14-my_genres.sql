-- Switch to the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select the genre names from tv_genres for the show Dexter
-- Use INNER JOIN to match the genre of Dexter with the genres in tv_genres
-- Order the results in ascending order by the genre name
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
