##Create the Employee table
CREATE TABLE Employee (
    id INTEGER NOT NULL UNIQUE,
    employee_id INTEGER NOT NULL UNIQUE,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    name VARCHAR(100),
    gender VARCHAR(10),
    location VARCHAR(100),
    PRIMARY KEY(id AUTOINCREMENT)
);
##Insert 10 rows of data
INSERT INTO Employee (employee_id, firstname, lastname, name, gender, location) VALUES
(1001, 'John', 'Doe', 'John Doe', 'Male', 'New York'),
(1002, 'Jane', 'Smith', 'Jane Smith', 'Female', 'Los Angeles'),
(1003, 'Alice', 'Johnson', 'Alice Johnson', 'Female', 'Chicago'),
(1004, 'Bob', 'Brown', 'Bob Brown', 'Male', 'Houston'),
(1005, 'Emma', 'Williams', 'Emma Williams', 'Female', 'Phoenix'),
(1006, 'Chris', 'Davis', 'Chris Davis', 'Male', 'Philadelphia'),
(1007, 'David', 'Miller', 'David Miller', 'Male', 'San Antonio'),
(1008, 'Sophia', 'Wilson', 'Sophia Wilson', 'Female', 'San Diego'),
(1009, 'Daniel', 'Moore', 'Daniel Moore', 'Male', 'Dallas'),
(1010, 'Olivia', 'Taylor', 'Olivia Taylor', 'Female', 'San Jose');
SELECT * FROM Employee
ALTER TABLE Employee DROP COLUMN id;



##Table structure for table attendance_tbl
CREATE TABLE attendance_tbl (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER NOT NULL,
  class_date DATE NOT NULL,
  status TINYINT NOT NULL, -- 1 = Present, 2 = Late, 3 = Absent, 4 = Holiday
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT NULL
);
###Dumping data for table attendance_tbl
INSERT INTO attendance_tbl (student_id, class_date, status, created_at, updated_at) VALUES
(4, '2023-11-30', 2, '2023-11-30 08:52:11', '2023-11-30 09:07:40'),
(3, '2023-11-30', 1, '2023-11-30 08:52:11', '2023-11-30 09:06:53'),
(1, '2023-11-30', 1, '2023-11-30 08:52:11', NULL),
(5, '2023-11-30', 3, '2023-11-30 08:52:11', '2023-11-30 09:07:40'),
(6, '2023-11-30', 1, '2023-11-30 08:52:11', '2023-11-30 09:06:53'),
(4, '2023-11-27', 4, '2023-11-30 09:08:16', NULL),
(3, '2023-11-27', 4, '2023-11-30 09:08:16', NULL),
(1, '2023-11-27', 4, '2023-11-30 09:08:16', NULL),
(5, '2023-11-27', 4, '2023-11-30 09:08:16', NULL);




## Table structure for table class_tbl
CREATE TABLE class_tbl (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT NULL
);

## Dumping data for table class_tbl
INSERT INTO class_tbl (name, created_at, updated_at) VALUES
('Grade 8-1 - English', '2023-11-16 11:37:26', '2023-11-16 11:52:34'),
('Grade 8-2 - English', '2023-11-16 11:52:46', NULL);


## Table structure for table students_tbl
CREATE TABLE students_tbl (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT NULL,
  FOREIGN KEY (class_id) REFERENCES class_tbl(id) ON DELETE CASCADE
);

##Dumping data for table students_tbl
INSERT INTO students_tbl (class_id, name, created_at, updated_at) VALUES
(1, 'John Smith', '2023-11-16 13:18:15', '2023-11-16 13:18:27'),
(1, 'John Doe', '2023-11-16 13:18:49', NULL),
(1, 'Claire Blake', '2023-11-16 13:18:56', NULL),
(1, 'Mark Cooper', '2023-11-16 13:19:18', NULL),
(1, 'Samantha Lou', '2023-11-16 13:19:30', NULL);

##create table for country

CREATE TABLE country (
  country_id SMALLINT NOT NULL,
  country VARCHAR(50) NOT NULL,
  last_update TIMESTAMP,
  PRIMARY KEY (country_id)
);

INSERT INTO country (country_id, country, last_update) VALUES
(1, 'United States', CURRENT_TIMESTAMP),
(2, 'Canada', CURRENT_TIMESTAMP),
(3, 'Mexico', CURRENT_TIMESTAMP),
(4, 'United Kingdom', CURRENT_TIMESTAMP);


CREATE TABLE Department (
    dept_id INTEGER NOT NULL UNIQUE,
    dept_name VARCHAR(100),
    employee_id INTEGER,
    PRIMARY KEY(dept_id)
);

INSERT INTO Department (dept_id, dept_name, employee_id) VALUES
(1, 'HR', 1001),
(2, 'Finance', 1002),
(3, 'IT', 1003),
(4, 'Marketing', 1004);



