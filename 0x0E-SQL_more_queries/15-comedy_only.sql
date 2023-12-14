-- Switch to the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;
-- Select the show titles from tv_shows that have the
-- genre Comedy
-- Use INNER JOIN to match the genre Comedy with
-- the genres in tv_genres
-- Order the results in ascending order by the show title
SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
