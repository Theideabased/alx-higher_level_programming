-- This will list the score greater than or equals to 10
USE hbtn_0c_0
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
