\pset pager off
SELECT 
    u.user_id,
    u.name,
    MAX(s.score_value) AS max_score
FROM users u
JOIN scores s ON u.user_id = s.user_id
GROUP BY u.user_id, u.name
ORDER BY max_score ASC;
