-- Lists all cities contained in the database hbtn_0d_usa.
-- One select
SELECT
  cities.id as id,
  cities.name as name,
  states.name as name
FROM cities
LEFT JOIN states
ON states.id = cities.state_id
ORDER BY cities.id ASC;
