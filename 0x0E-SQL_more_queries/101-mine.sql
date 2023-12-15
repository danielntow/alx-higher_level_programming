-- Get the genre_id for Comedy
SET @comedy_genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- Select all shows without the Comedy genre
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = @comedy_genre_id
)
ORDER BY title ASC;

