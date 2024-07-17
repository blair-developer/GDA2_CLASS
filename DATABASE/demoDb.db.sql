BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "attendance_tbl" (
	"id"	INTEGER,
	"student_id"	INTEGER NOT NULL,
	"class_date"	DATE NOT NULL,
	"status"	TINYINT NOT NULL,
	"created_at"	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updated_at"	DATETIME DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "class_tbl" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"created_at"	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updated_at"	DATETIME DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Department" (
	"dept_id"	INTEGER NOT NULL UNIQUE,
	"dept_name"	VARCHAR(100),
	"employee_id"	INTEGER,
	PRIMARY KEY("dept_id")
);
CREATE TABLE IF NOT EXISTS "Employee" (
	"id"	INTEGER NOT NULL UNIQUE,
	"employee_id"	INTEGER,
	"firstname"	VARCHAR(50),
	"lastname"	VARCHAR(50),
	"name"	VARCHAR(100),
	"gender"	VARCHAR(10),
	"location"	VARCHAR(100),
	"age"	INT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Employee_backup" (
	"id"	INT,
	"employee_id"	INT,
	"firstname"	TEXT,
	"lastname"	TEXT,
	"name"	TEXT,
	"gender"	TEXT,
	"location"	TEXT,
	"age"	INT
);
CREATE TABLE IF NOT EXISTS "students_tbl" (
	"id"	INTEGER,
	"class_id"	INTEGER COLLATE UTF16CI,
	"name"	TEXT,
	"created_at"	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COLLATE UTF16CI,
	"updated_at"	DATETIME DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "attendance_tbl" VALUES (1,4,'2023-11-30',2,'2023-11-30 08:52:11','2023-11-30 09:07:40');
INSERT INTO "attendance_tbl" VALUES (2,3,'2023-11-30',1,'2023-11-30 08:52:11','2023-11-30 09:06:53');
INSERT INTO "attendance_tbl" VALUES (3,1,'2023-11-30',1,'2023-11-30 08:52:11',NULL);
INSERT INTO "attendance_tbl" VALUES (4,5,'2023-11-30',3,'2023-11-30 08:52:11','2023-11-30 09:07:40');
INSERT INTO "attendance_tbl" VALUES (5,6,'2023-11-30',1,'2023-11-30 08:52:11','2023-11-30 09:06:53');
INSERT INTO "attendance_tbl" VALUES (6,4,'2023-11-27',4,'2023-11-30 09:08:16',NULL);
INSERT INTO "attendance_tbl" VALUES (7,3,'2023-11-27',4,'2023-11-30 09:08:16',NULL);
INSERT INTO "attendance_tbl" VALUES (8,1,'2023-11-27',4,'2023-11-30 09:08:16',NULL);
INSERT INTO "attendance_tbl" VALUES (9,5,'2023-11-27',4,'2023-11-30 09:08:16',NULL);
INSERT INTO "class_tbl" VALUES (1,'Grade 8-1','2023-11-16 11:37:26','2023-11-16 11:52:34');
INSERT INTO "class_tbl" VALUES (2,'Grade 8-2','2023-11-16 11:52:46',NULL);
INSERT INTO "class_tbl" VALUES (3,'Grade 7-1','2023-11-16 11:37:26','2023-11-16 11:52:34');
INSERT INTO "class_tbl" VALUES (4,'Grade 7-2','2023-11-16 11:52:46',NULL);
INSERT INTO "class_tbl" VALUES (5,'Grade 7-1','2023-11-16 11:37:26','2023-11-16 11:52:34');
INSERT INTO "class_tbl" VALUES (6,'Grade 7-2','2023-11-16 11:52:46',NULL);
INSERT INTO "class_tbl" VALUES (7,'Grade 6-1','2023-11-16 11:37:26','2023-11-16 11:52:34');
INSERT INTO "class_tbl" VALUES (8,'Grade 6-2','2023-11-16 11:52:46',NULL);
INSERT INTO "Department" VALUES (1,'HR',1001);
INSERT INTO "Department" VALUES (2,'Finance',1002);
INSERT INTO "Department" VALUES (3,'IT',1003);
INSERT INTO "Department" VALUES (4,'Marketing',1004);
INSERT INTO "Employee" VALUES (1,1001,'John','Doe','John Doe','Male','New York',30);
INSERT INTO "Employee" VALUES (2,1002,'Jane','Smith','Jane Smith','Female','Los Angeles',25);
INSERT INTO "Employee" VALUES (3,1003,'Alice','Johnson','Alice Johnson','Female','Chicago',35);
INSERT INTO "Employee" VALUES (4,1004,'Bob','Brown','Bob Brown','Male','Houston',28);
INSERT INTO "Employee" VALUES (5,1001,'Emma','Williams','Emma Williams','Female','Phoenix',32);
INSERT INTO "Employee" VALUES (6,1002,'Chris','Davis','Chris Davis','Male','Philadelphia',29);
INSERT INTO "Employee" VALUES (7,1003,'David','Miller','David Miller','Male','San Antonio',40);
INSERT INTO "Employee" VALUES (8,1004,'Sophia','Wilson','Sophia Wilson','Female','San Diego',22);
INSERT INTO "Employee" VALUES (9,1005,'Daniel','Moore','Daniel Moore','Male','Dallas',34);
INSERT INTO "Employee" VALUES (10,1001,'Olivia','Taylor','Olivia Taylor','Female','San Jose',27);
INSERT INTO "Employee" VALUES (11,1002,'Liam','Johnson','Liam Johnson','Male','Boston',31);
INSERT INTO "Employee_backup" VALUES (1,1001,'John','Doe','John Doe','Male','New York',30);
INSERT INTO "Employee_backup" VALUES (2,1002,'Jane','Smith','Jane Smith','Female','Los Angeles',25);
INSERT INTO "Employee_backup" VALUES (3,1003,'Alice','Johnson','Alice Johnson','Female','Chicago',35);
INSERT INTO "Employee_backup" VALUES (4,1004,'Bob','Brown','Bob Brown','Male','Houston',28);
INSERT INTO "Employee_backup" VALUES (5,1001,'Emma','Williams','Emma Williams','Female','Phoenix',32);
INSERT INTO "Employee_backup" VALUES (6,1002,'Chris','Davis','Chris Davis','Male','Philadelphia',29);
INSERT INTO "Employee_backup" VALUES (7,1003,'David','Miller','David Miller','Male','San Antonio',40);
INSERT INTO "Employee_backup" VALUES (8,1004,'Sophia','Wilson','Sophia Wilson','Female','San Diego',22);
INSERT INTO "Employee_backup" VALUES (9,1005,'Daniel','Moore','Daniel Moore','Male','Dallas',34);
INSERT INTO "Employee_backup" VALUES (10,1001,'Olivia','Taylor','Olivia Taylor','Female','San Jose',27);
INSERT INTO "Employee_backup" VALUES (11,1002,'Liam','Johnson','Liam Johnson','Male','Boston',31);
INSERT INTO "students_tbl" VALUES (1,1,'John Smith','2023-11-16 13:18:15','2023-11-16 13:18:27');
INSERT INTO "students_tbl" VALUES (2,1,'John Doe','2023-11-16 13:18:49',NULL);
INSERT INTO "students_tbl" VALUES (3,1,'Claire Blake','2023-11-16 13:18:56',NULL);
INSERT INTO "students_tbl" VALUES (4,1,'Mark Cooper','2023-11-16 13:19:18',NULL);
INSERT INTO "students_tbl" VALUES (5,1,'Samantha Lou','2023-11-16 13:19:30',NULL);
INSERT INTO "students_tbl" VALUES (6,6,'Liam Johnson','2023-11-16 13:18:15','2023-11-16 13:18:27');
INSERT INTO "students_tbl" VALUES (7,7,'Emma Brown','2023-11-16 13:18:49',NULL);
INSERT INTO "students_tbl" VALUES (8,8,'Noah Davis','2023-11-16 13:18:56',NULL);
INSERT INTO "students_tbl" VALUES (9,9,'Olivia Miller','2023-11-16 13:19:18',NULL);
INSERT INTO "students_tbl" VALUES (10,10,'Ava Wilson','2023-11-16 13:19:30',NULL);
INSERT INTO "students_tbl" VALUES (11,2,'tonny Johnson','2023-11-16 13:18:15','2023-11-16 13:18:27');
INSERT INTO "students_tbl" VALUES (12,2,'omondi Brown','2023-11-16 13:18:49',NULL);
INSERT INTO "students_tbl" VALUES (13,3,'derrick Davis','2023-11-16 13:18:56',NULL);
INSERT INTO "students_tbl" VALUES (14,4,'cliff Miller','2023-11-16 13:19:18',NULL);
INSERT INTO "students_tbl" VALUES (15,3,'weruty Wilson','2023-11-16 13:19:30',NULL);
COMMIT;
