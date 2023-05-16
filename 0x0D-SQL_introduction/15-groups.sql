-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
-- Select with count and group by
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score;

