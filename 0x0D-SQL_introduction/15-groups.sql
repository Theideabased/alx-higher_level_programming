-- this will count a score according to how many time they occur
SELECT score
COUNT(score) as number
FROM second_table
GROUP BY score;
