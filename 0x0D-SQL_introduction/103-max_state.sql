-- displays the max temperature of each state (ordered by State name).
-- Select with max
SELECT
state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC
LIMIT 3;

