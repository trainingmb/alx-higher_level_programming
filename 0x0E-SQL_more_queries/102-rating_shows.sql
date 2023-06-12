-- Lists all shows from hbtn_0d_tvshows_rate by their rating
-- Only One
SELECT
  tv_shows.title,
  SUM(tv_show_ratings.rate) AS rating
FROM
  tv_show_ratings
LEFT JOIN
  tv_shows ON
    tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_show_ratings.show_id
ORDER BY 2 DESC;
