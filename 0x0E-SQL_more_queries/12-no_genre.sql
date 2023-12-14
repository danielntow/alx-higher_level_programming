-- Switch to the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select the title from tv_shows where there is no matching show_id in tv_show_genres
-- Order the results by tv_shows.title in ascending order
SELECT tv_shows.title , tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
