# 📘 Experiment No. 1 – Database Management System (DBMS)

## **Topic:**

**SQL Queries using DDL, DML, Operators, Functions, and SQL Objects**

---

## **🎯 Aim**

To study and execute SQL queries using **Data Definition Language (DDL)**, **Data Manipulation Language (DML)**, **operators**, **functions**, and **SQL objects** such as **views** and **indexes**.

---

## **📚 Objectives**

* To create and manage databases and tables using DDL commands.
* To perform insert, update, delete, and select operations using DML commands.
* To apply SQL operators and aggregate functions.
* To understand and implement SQL objects such as **views**, **indexes**, and **auto-increment** fields.

---

## **🧩 Theory**

### **1. Data Definition Language (DDL)**

* Defines the structure of the database.
* Common commands:
  `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.

### **2. Data Manipulation Language (DML)**

* Used to manipulate data stored in tables.
* Common commands:
  `INSERT`, `UPDATE`, `DELETE`, `SELECT`.

### **3. SQL Operators**

* Used in queries for filtering or comparing data.
  Examples: `=`, `<`, `>`, `BETWEEN`, `AND`, `OR`, `LIKE`.

### **4. SQL Functions**

* Built-in functions used to perform calculations on data.
  Examples: `COUNT()`, `AVG()`, `SUM()`, `MAX()`, `MIN()`.

### **5. SQL Objects**

* **Views:** Virtual tables created from queries.
* **Indexes:** Improve the speed of data retrieval.
* **Sequences / Auto-Increment:** Automatically generate unique IDs for records.

---

## **💻 Code Implementation**

```sql
/* ============================================================
   Experiment No. 1 - Database Management System (DBMS)
   Topic: SQL Queries using DDL, DML, Operators, Functions, and SQL Objects
   ============================================================ */

/* ---------- DATABASE CREATION ---------- */
CREATE DATABASE student_db;
USE student_db;

/* ---------- TABLE CREATION WITH CONSTRAINTS ---------- */
CREATE TABLE student (
  roll_no INT PRIMARY KEY,
  student_name VARCHAR(50) NOT NULL,
  student_department VARCHAR(50) NOT NULL,
  student_address VARCHAR(50),
  student_marks INT CHECK (student_marks BETWEEN 0 AND 100)
);

/* ---------- DATA INSERTION ---------- */
INSERT INTO student VALUES (25, 'Kiran', 'Civil', 'Kolhapur', 31);
INSERT INTO student VALUES (20, 'Prathamesh', 'AIDS', 'Pune', 30);
INSERT INTO student VALUES (29, 'Rahul', 'IT', 'Thane', 30);
INSERT INTO student VALUES (23, 'Om', 'ENTC', 'Pune', 29);
INSERT INTO student VALUES (21, 'Rohit', 'CSE', 'Mumbai', 28);
INSERT INTO student VALUES (24, 'Priya', 'Mechanical', 'Nashik', 27);
INSERT INTO student VALUES (26, 'Anjali', 'Electrical', 'Aurangabad', 26);
INSERT INTO student VALUES (22, 'Snehal', 'IT', 'Nagpur', 25);
INSERT INTO student VALUES (28, 'Neha', 'CSE', 'Pune', 24);

/* ============================================================
   SQL QUERIES WITH EXPLANATIONS
   ============================================================ */

/* 1. Display all student records */
SELECT * FROM student;

/* 2. Display students from Pune */
SELECT * FROM student WHERE student_address = 'Pune';

/* 3. Display students having marks greater than 28 */
SELECT student_name, student_marks FROM student WHERE student_marks > 28;

/* 4. Display students sorted by marks in descending order */
SELECT * FROM student ORDER BY student_marks DESC;

/* 5. Count number of students per department */
SELECT student_department, COUNT(*) AS total_students 
FROM student 
GROUP BY student_department;

/* 6. Find average marks of students in each department */
SELECT student_department, AVG(student_marks) AS avg_marks 
FROM student 
GROUP BY student_department;

/* 7. Find students having marks between 25 and 30 */
SELECT * FROM student WHERE student_marks BETWEEN 25 AND 30;

/* 8. Update marks of student “Neha” by +5 */
UPDATE student SET student_marks = student_marks + 5 WHERE student_name = 'Neha';

/* 9. Delete record of student “Anjali” */
DELETE FROM student WHERE student_name = 'Anjali';

/* 10. Create a view to show only CSE students */
CREATE VIEW cse_students AS
SELECT roll_no, student_name, student_marks FROM student 
WHERE student_department = 'CSE';

/* 11. Create an index for faster search by department */
CREATE INDEX idx_department ON student(student_department);

/* 12. Create table using Auto Increment (sequence-like behavior) */
CREATE TABLE student_seq (
  roll_no INT AUTO_INCREMENT PRIMARY KEY,
  student_name VARCHAR(50),
  student_department VARCHAR(50)
);

/* Insert values into auto increment table */
INSERT INTO student_seq (student_name, student_department)
VALUES ('Kiran', 'Civil'), ('Rohit', 'CSE');

/* 13. Create synonym-like view (MySQL alternative) */
CREATE VIEW stud AS SELECT * FROM student;

/* Display data from synonym view */
SELECT * FROM stud;

/* 14. Calculate total marks of all students */
SELECT SUM(student_marks) AS total_marks FROM student;

/* 15. Display the student(s) with the highest marks */
SELECT student_name, student_marks FROM student
WHERE student_marks = (SELECT MAX(student_marks) FROM student);

/* ============================================================
   CONCLUSION
   ============================================================
   ✓ Successfully implemented DDL and DML commands.
   ✓ Executed queries using operators, aggregate functions, and grouping.
   ✓ Created and tested SQL objects: Views, Indexes, Auto-Increment.
   ✓ Demonstrated efficient SQL query writing and database management.
   ============================================================ */

```

## **✅ Conclusion**

We successfully executed SQL queries using **DDL**, **DML**, **operators**, **functions**, and **SQL objects**.
This experiment demonstrated:

* Database and table creation with constraints.
* Data manipulation (insert, update, delete, select).
* Use of aggregate functions and grouping.
* Implementation of views, indexes, and auto-increment fields.

Thus, we efficiently understood and practiced **SQL query writing and database management**.