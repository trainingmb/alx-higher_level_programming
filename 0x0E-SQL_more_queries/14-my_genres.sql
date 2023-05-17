-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- The Select
SELECT
	tv_genres.name as genre
FROM
tv_show_genres
LEFT JOIN tv_genres ON
tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows ON
tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter";
