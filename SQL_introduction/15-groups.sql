-- GROUPS
SELECT score, COUNT(*) FROM second_table GROUP BY score HAVING COUNT(*) > 1;