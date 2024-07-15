#Create Employee_backup table and insert data
CREATE TABLE Employee_backup AS SELECT * FROM Employee;

# Find identical rows in Employee and Employee_backup
SELECT e.*
FROM Employee e
JOIN Employee_backup eb ON e.employee_id = eb.employee_id AND e.firstname = eb.firstname AND e.lastname = eb.lastname;

#Joining Tables Using Aggregate Functions
#To find the total number of students in each class:

SELECT c.name AS class_name, COUNT(s.id) AS total_students
FROM class_tbl c
JOIN students_tbl s ON c.id = s.class_id
GROUP BY c.id;

#to replace a column nameUPDATE class_tbl
SET name = REPLACE(name, ' - English', '');

#To find the total attendance status for each student:

SELECT s.name AS student_name, 
       SUM(CASE WHEN a.status = 1 THEN 1 ELSE 0 END) AS present,
       SUM(CASE WHEN a.status = 2 THEN 1 ELSE 0 END) AS late,
       SUM(CASE WHEN a.status = 3 THEN 1 ELSE 0 END) AS absent,
       SUM(CASE WHEN a.status = 4 THEN 1 ELSE 0 END) AS holiday
FROM students_tbl s
JOIN attendance_tbl a ON s.id = a.student_id
GROUP BY s.id;

#Concept 4: Working with Multiple Tables
#To retrieve detailed employee information along with their department name:
SELECT e.firstname, e.lastname, e.location, d.dept_name
FROM Employee e
JOIN Department d ON e.employee_id = d.employee_id;

#To find the attendance status of students along with their class names:
SELECT s.name AS student_name, c.name AS class_name, a.class_date, a.status
FROM students_tbl s
JOIN class_tbl c ON s.class_id = c.id
JOIN attendance_tbl a ON s.id = a.student_id;


