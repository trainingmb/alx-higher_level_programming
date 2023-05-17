-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- Super Query
SELECT id, name
FROM cities
WHERE state_id = 
-- Subquery
(SELECT id
  FROM states
  WHERE name = "California"
  LIMIT 1)
ORDER BY id;
