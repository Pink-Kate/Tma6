SELECT t.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.id = 1
GROUP BY t.name;
