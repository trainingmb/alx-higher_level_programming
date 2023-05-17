-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Only One Select
SELECT
  tv_genres.name,
  SUM(tv_show_ratings.rate)
FROM
  tv_show_genres
LEFT JOIN
  tv_genres ON
    tv_show_genres.genre_id = tv_genres.id
LEFT JOIN
  tv_show_ratings ON
    tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre_id
ORDER BY 2 DESC;
