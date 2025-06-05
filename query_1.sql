SELECT students.name, ROUND(AVG(grade), 2) as avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 5;
