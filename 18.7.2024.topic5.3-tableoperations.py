--how many employees are in each Department
SELECT d.dept_name, COUNT(e.employee_id) AS number_of_employees
FROM Department d
INNER JOIN Employee e ON d.employee_id = e.employee_id
GROUP BY d.dept_name

--which employees work in the IT departent
SELECT e.name, e.gender, d.dept_name
FROM Employee e
JOIN Department d ON d.employee_id = d.employee_id
WHERE d.dept_name = "IT"

--employees who are located in nairobi and mombasa with their departments
SELECT e.name, e.location, d.dept_name, e.age
FROM Employee e
JOIN Department d ON d.employee_id = d.employee_id
WHERE e.location IN("Phoenix","Mombasa") AND e.age BETWEEN 30 AND 32

--which clases have students marked as late= STATUS2
SELECT DISTINCT c.name
FROM class_tbl c
JOIN students_tbl s ON c.id = s.class_id
JOIN attendance_tbl a ON s.id = a.student_id
WHERE a.status = 2

