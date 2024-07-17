--TABLE OPERATIONS
SELECT * FROM Department

--FIND FEMALE EMPLOYEES
SELECT * FROM Employee
WHERE gender = "Male" AND age BETWEEN 30 AND 35

--ALTER TABLE COLUMN name
UPDATE Employee
SET location = "Mombasa"
WHERE employee_id = 1003

--ALTER TABLE employee
ALTER TABLE Employee
ADD DateOfBirth date;

--drop COLUMN in a table
ALTER TABLE Employee
DROP DateOfBirth;

--WORKING WITH MULTIPLE TABLES
CREATE TABLE Employee_backup AS SELECT * FROM Employee;

--FINDING IDENTICAL ROWS IN EMPLOYEE AND Employee_backup/department TABLE
SELECT e.*
from Employee AS e
INNER JOIN Department AS d ON e.employee_id = d.employee_id

SELECT e.name
from Employee AS e
INNER JOIN Department AS d ON e.employee_id = d.employee_id
WHERE e.employee_id = 1003

--join tables using aggregate functions.
--find the total number of students in each class
SELECT c.name AS Class_name, COUNT(s.id) AS Total_students
FROM class_tbl AS c
INNER JOIN students_tbl AS s ON c.id = s.class_id
WHERE c.name = "Grade 8-2"
GROUP BY c.id;

--to find the total attendance status for each student ## not working with alias on table naming
SELECT s.name AS student_name,
   SUM(CASE WHEN a.status = 1 THEN 1 ELSE 0 END) AS present,
   SUM(CASE WHEN a.status  = 2 THEN 1 ELSE 0 END) AS late,
   SUM(CASE WHEN a.status  = 3 THEN 1 ELSE 0 END) AS absent,
   SUM(CASE WHEN a.status  = 4 THEN 1 ELSE 0 END) AS holiday
FROM students_tbl AS s   
JOIN attendance_tbl AS a ON s.id = a.student_id
GROUP BY s.id;

--working with multiple table(complex joins)
SELECT e.name, e.gender, e.location, d.dept_name
FROM Employee AS e
INNER JOIN Department AS d ON e.employee_id = d.employee_id
WHERE dept_name = "HR"




