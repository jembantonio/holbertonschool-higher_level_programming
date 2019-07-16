-- a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id
