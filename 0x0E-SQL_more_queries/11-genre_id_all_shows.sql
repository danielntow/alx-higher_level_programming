-- Switch to the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select the title from tv_shows and genre_id from tv_show_genres
-- Use a LEFT JOIN to include shows without genres
-- Order the results by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, COALESCE(tv_show_genres.genre_id, 'NULL') ASC;
