SELECT gr.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Math'
GROUP BY gr.id;
