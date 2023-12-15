USE hbtn_0d_tvshows;

SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;


USE hbtn_0d_tvshows;

SELECT title, NULL AS genre_id
FROM tv_shows
WHERE NOT EXISTS (SELECT 1 FROM tv_show_genres WHERE show_id = tv_shows.id)
ORDER BY title ASC;


USE hbtn_0d_tvshows;

SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id AND tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;


SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT show_id FROM tv_show_genres)
ORDER BY tv_shows.title ASC;
