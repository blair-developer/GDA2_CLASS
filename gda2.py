##Selecting all rows from the 'employees' table either stidents tables---
SELECT * FROM Employee;

##Selecting all rows from the 'employees' table either stidents tables---
##order By DESC, ASC. GROUP BY, HAVING 
SELECT * FROM Employee;

##The IN operator allows you to specify multiple values in a WHERE clause.
SELECT * FROM Employee
WHERE location IN ("Chicago", "Houston");

##INSERT A COLUMN AND ROWS using ALTER
ALTER TABLE Employee ADD COLUMN age INT;
UPDATE Employee SET age = 30 WHERE id = 1;
UPDATE Employee SET age = 25 WHERE id = 2;
UPDATE Employee SET age = 35 WHERE id = 3;
UPDATE Employee SET age = 28 WHERE id = 4;
UPDATE Employee SET age = 32 WHERE id = 5;
UPDATE Employee SET age = 29 WHERE id = 6;
UPDATE Employee SET age = 40 WHERE id = 7;
UPDATE Employee SET age = 22 WHERE id = 8;
UPDATE Employee SET age = 34 WHERE id = 9;
UPDATE Employee SET age = 27 WHERE id = 10;


##insert a row in an employee table
INSERT INTO Employee (employee_id, firstname, lastname, name, gender, location, age) 
VALUES (1011, 'Liam', 'Johnson', 'Liam Johnson', 'Male', 'Boston', 31);

##Selecting specific columns from the 'employees' table
SELECT employee_id, firstname FROM Employee;


##Selecting rows with a condition
##Example: Finding EMPLOYEE older than 30
SELECT * FROM Employee WHERE age > 30;
##Example: Finding EMPLOYEE in a specific LOCATION
SELECT * FROM Employee WHERE  location= 'Chicago';


##Selecting rows where a column has NULL value
##Example: Finding attendance without date
SELECT * FROM attendance_tbl WHERE updated_at IS NULL;


##Combining two columns into a full name while selecting distinct column
SELECT employee_id, firstname || ' ' || lastname AS full_name FROM Employee;


#Limiting the number of returned rows
#Example: Getting the first 5 employees
SELECT * FROM Employee LIMIT 5;


#Sorting query result
#Example: Sorting employees by age in ascending order
SELECT * FROM Employee ORDER BY age ASC;
#Example: Sorting students by age in descending order
SELECT * FROM Employee ORDER BY age DESC;


##Example: Selecting rows with gender conditions
SELECT * FROM Employee WHERE gender = 'Male';
##Example: Selecting rows with integer and string conditions
SELECT * FROM Employee WHERE age = 20 AND firstname = 'David';


##Perform inner join and select distinct columns
##INNER JOIN is a type of join that returns only the rows where there is a match between the tables being joined.
SELECT DISTINCT e.firstname, d.dept_name
FROM Employee e
INNER JOIN Department d ON e.employee_id = d.employee_id;



##question to take home

Write a SQL query to find and list the full names, gender, and location of employees who are between 20 and 35 years old, and whose location is "New York". 
Ensure that only the full names, gender, and location of these employees are displayed in the result.

answer::::
      SELECT name, gender, location
FROM Employee
WHERE age BETWEEN 20 AND 35
  AND location = 'New York';


