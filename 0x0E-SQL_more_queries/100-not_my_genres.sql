-- List all genres not linked to the show Dexter
-- Max of 2 Selects
SELECT
tv_genres.name
FROM 
tv_genres
WHERE
tv_genres.id NOT IN(
  SELECT
    tv_show_genres.genre_id
  FROM
    tv_show_genres
  INNER JOIN
    tv_shows ON
    tv_show_genres.show_id = tv_shows.id
  WHERE
    tv_shows.title = "Dexter")
ORDER by tv_genres.name;
    
