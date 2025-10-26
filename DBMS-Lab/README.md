# DBMS Mock Practical - Quick Learning Guide

I'll create a comprehensive guide to help you prepare for your DBMS practical exam covering all 6 experiments.

---

## 📋 **Experiment Overview**

1. **SQL Queries (DDL & DML)**
2. **SQL Joins, Sub-Queries & Views**
3. **MongoDB CRUD Operations**
4. **PL/SQL Control Structures & Exception Handling**
5. **PL/SQL Cursors**
6. **Database Connectivity with Front-end**

---

## 🎯 **Experiment 1: SQL DDL & DML Commands**

### **Key Concepts to Remember**

**DDL Commands:**
- `CREATE` - Create database objects
- `ALTER` - Modify structure
- `DROP` - Delete objects
- `TRUNCATE` - Remove all records

**DML Commands:**
- `SELECT` - Retrieve data
- `INSERT` - Add records
- `UPDATE` - Modify records
- `DELETE` - Remove records

### **Important Constraints**
```sql
-- Primary Key
employee_id INT PRIMARY KEY

-- Foreign Key
FOREIGN KEY (department_id) REFERENCES departments(department_id)

-- Unique
email VARCHAR(100) UNIQUE

-- Check
CHECK (salary >= 0)

-- Not Null
name VARCHAR(50) NOT NULL
```

### **Common Query Patterns**
```sql
-- Basic SELECT with WHERE
SELECT * FROM employees WHERE salary > 50000;

-- ORDER BY
SELECT * FROM employees ORDER BY salary DESC;

-- GROUP BY with HAVING
SELECT dept, AVG(salary) 
FROM employees 
GROUP BY dept 
HAVING AVG(salary) > 30000;

-- Aggregate Functions
SELECT COUNT(*), SUM(salary), AVG(salary), MAX(salary), MIN(salary)
FROM employees;
```

### **Index & View**
```sql
-- Create Index
CREATE INDEX idx_name ON table_name(column_name);

-- Create View
CREATE VIEW employee_view AS 
SELECT emp_id, name, salary FROM employees WHERE dept = 'IT';
```

---

## 🎯 **Experiment 2: Joins, Sub-Queries & Views**

### **Types of Joins**

```sql
-- INNER JOIN (matching records only)
SELECT o.OrderID, c.CustomerName 
FROM Orders o 
INNER JOIN Customers c ON o.CustomerID = c.CustomerID;

-- LEFT JOIN (all from left table)
SELECT e.name, d.dept_name 
FROM employees e 
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- RIGHT JOIN (all from right table)
SELECT e.name, d.dept_name 
FROM employees e 
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- FULL OUTER JOIN (all from both)
SELECT e.name, d.dept_name 
FROM employees e 
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;
```

### **Sub-Queries**
```sql
-- Single-row subquery
SELECT name FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Multi-row subquery with IN
SELECT name FROM employees 
WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'Mumbai');

-- Correlated subquery
SELECT e1.name, e1.salary 
FROM employees e1 
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.dept_id = e1.dept_id);
```

### **Views Operations**
```sql
-- Create View
CREATE VIEW high_salary_emp AS 
SELECT * FROM employees WHERE salary > 50000;

-- Update View
CREATE OR REPLACE VIEW high_salary_emp AS 
SELECT emp_id, name, salary, dept FROM employees WHERE salary > 60000;

-- Drop View
DROP VIEW high_salary_emp;
```

---

## 🎯 **Experiment 3: MongoDB CRUD Operations**

### **Basic Commands**
```javascript
// Create Database
use college

// Create Collection
db.createCollection("students")

// INSERT (Create)
db.students.insert({
    roll_no: 1,
    name: "John",
    dept: "CS",
    marks: 85
})

// INSERT Multiple
db.students.insertMany([
    {roll_no: 2, name: "Alice", dept: "IT"},
    {roll_no: 3, name: "Bob", dept: "CS"}
])

// FIND (Read)
db.students.find()                          // All documents
db.students.find().pretty()                 // Formatted output
db.students.find({dept: "CS"})              // With condition
db.students.findOne({roll_no: 1})           // Single document

// UPDATE
db.students.update(
    {roll_no: 1},                           // Filter
    {$set: {marks: 90}}                     // Update
)

// Update Multiple
db.students.updateMany(
    {dept: "CS"},
    {$set: {status: "Active"}}
)

// DELETE
db.students.remove({roll_no: 1})            // Delete specific
db.students.remove({})                       // Delete all
```

### **Logical Operators**
```javascript
// AND
db.students.find({dept: "CS", marks: {$gt: 80}})

// OR
db.students.find({
    $or: [
        {dept: "CS"},
        {marks: {$gt: 90}}
    ]
})

// AND + OR Combined
db.students.find({
    marks: {$gt: 70},
    $or: [{dept: "CS"}, {dept: "IT"}]
})
```

### **Comparison Operators**
- `$eq` - Equal to
- `$gt` - Greater than
- `$gte` - Greater than or equal
- `$lt` - Less than
- `$lte` - Less than or equal
- `$ne` - Not equal

---

## 🎯 **Experiment 4: PL/SQL Control Structures & Exception Handling**

### **Basic Structure**
```sql
DECLARE
    -- Variable declarations
    v_name VARCHAR2(50);
    v_salary NUMBER;
BEGIN
    -- Executable statements
    SELECT name, salary INTO v_name, v_salary 
    FROM employees WHERE emp_id = 101;
    
    DBMS_OUTPUT.PUT_LINE('Name: ' || v_name);
EXCEPTION
    -- Exception handling
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Employee not found');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error occurred');
END;
/
```

### **Control Structures**

**IF-THEN-ELSE:**
```sql
IF attendance < 75 THEN
    status := 'Detained';
ELSIF attendance >= 75 AND attendance < 85 THEN
    status := 'Pass';
ELSE
    status := 'Good';
END IF;
```

**CASE:**
```sql
CASE grade
    WHEN 'A' THEN bonus := salary * 0.2;
    WHEN 'B' THEN bonus := salary * 0.1;
    ELSE bonus := 0;
END CASE;
```

**SIMPLE LOOP:**
```sql
LOOP
    counter := counter + 1;
    EXIT WHEN counter > 10;
END LOOP;
```

**WHILE LOOP:**
```sql
WHILE counter <= 10 LOOP
    counter := counter + 1;
END LOOP;
```

**FOR LOOP:**
```sql
FOR i IN 1..10 LOOP
    DBMS_OUTPUT.PUT_LINE('Count: ' || i);
END LOOP;
```

### **Exception Handling**
```sql
DECLARE
    v_balance NUMBER;
    insufficient_funds EXCEPTION;  -- User-defined
BEGIN
    SELECT balance INTO v_balance FROM accounts WHERE acc_no = 101;
    
    IF v_balance < 1000 THEN
        RAISE insufficient_funds;
    END IF;
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Account not found');
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Multiple accounts found');
    WHEN insufficient_funds THEN
        DBMS_OUTPUT.PUT_LINE('Insufficient balance');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Unknown error: ' || SQLERRM);
END;
```

### **Common Predefined Exceptions**
- `NO_DATA_FOUND` - SELECT returns no rows
- `TOO_MANY_ROWS` - SELECT returns multiple rows
- `ZERO_DIVIDE` - Division by zero
- `VALUE_ERROR` - Arithmetic/conversion error
- `INVALID_CURSOR` - Invalid cursor operation

---

## 🎯 **Experiment 5: PL/SQL Cursors**

### **Implicit Cursor**
```sql
BEGIN
    UPDATE employees SET salary = salary * 1.1;
    
    IF SQL%FOUND THEN
        DBMS_OUTPUT.PUT_LINE(SQL%ROWCOUNT || ' rows updated');
    END IF;
END;
```

### **Explicit Cursor - Simple Loop**
```sql
DECLARE
    CURSOR emp_cursor IS SELECT emp_id, name FROM employees;
    v_emp_id employees.emp_id%TYPE;
    v_name employees.name%TYPE;
BEGIN
    OPEN emp_cursor;
    LOOP
        FETCH emp_cursor INTO v_emp_id, v_name;
        EXIT WHEN emp_cursor%NOTFOUND;
        
        DBMS_OUTPUT.PUT_LINE(v_emp_id || ' - ' || v_name);
    END LOOP;
    CLOSE emp_cursor;
END;
```

### **Cursor with WHILE Loop**
```sql
DECLARE
    CURSOR emp_cursor IS SELECT * FROM employees;
    emp_rec employees%ROWTYPE;
BEGIN
    OPEN emp_cursor;
    FETCH emp_cursor INTO emp_rec;
    
    WHILE emp_cursor%FOUND LOOP
        DBMS_OUTPUT.PUT_LINE(emp_rec.name);
        FETCH emp_cursor INTO emp_rec;
    END LOOP;
    
    CLOSE emp_cursor;
END;
```

### **Cursor FOR Loop** (Easiest - No OPEN/FETCH/CLOSE needed)
```sql
DECLARE
    CURSOR emp_cursor IS SELECT * FROM employees;
BEGIN
    FOR emp_rec IN emp_cursor LOOP
        DBMS_OUTPUT.PUT_LINE(emp_rec.name || ' - ' || emp_rec.salary);
    END LOOP;
END;
```

### **Parameterized Cursor**
```sql
DECLARE
    CURSOR dept_cursor(p_dept VARCHAR2) IS 
        SELECT * FROM employees WHERE dept = p_dept;
BEGIN
    FOR emp_rec IN dept_cursor('CS') LOOP
        DBMS_OUTPUT.PUT_LINE(emp_rec.name);
    END LOOP;
    
    FOR emp_rec IN dept_cursor('IT') LOOP
        DBMS_OUTPUT.PUT_LINE(emp_rec.name);
    END LOOP;
END;
```

### **Cursor Attributes**
- `%FOUND` - TRUE if fetch returned a row
- `%NOTFOUND` - TRUE if fetch didn't return a row
- `%ISOPEN` - TRUE if cursor is open
- `%ROWCOUNT` - Number of rows fetched

---

## 🎯 **Experiment 6: Database Connectivity**

### **JDBC Connection (Java + MySQL)**

```java
import java.sql.*;

public class DBConnection {
    public static void main(String[] args) {
        try {
            // 1. Load Driver
            Class.forName("com.mysql.jdbc.Driver");
            
            // 2. Create Connection
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/college", 
                "root", 
                "password"
            );
            
            // 3. Create Statement
            Statement stmt = con.createStatement();
            
            // INSERT
            String insertQuery = "INSERT INTO students VALUES(1, 'John', 'CS')";
            stmt.executeUpdate(insertQuery);
            
            // SELECT
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            while(rs.next()) {
                System.out.println(rs.getInt(1) + " " + rs.getString(2));
            }
            
            // UPDATE
            stmt.executeUpdate("UPDATE students SET name='Alice' WHERE id=1");
            
            // DELETE
            stmt.executeUpdate("DELETE FROM students WHERE id=1");
            
            // 4. Close Connection
            con.close();
            
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
```

---

## 📝 **VIVA Questions & Answers**

### **General DBMS Concepts**

**Q1: What is DBMS?**
**A:** Database Management System is software that manages databases, providing data storage, retrieval, and manipulation while ensuring data security, integrity, and consistency.

**Q2: What is the difference between DDL and DML?**
**A:** 
- **DDL (Data Definition Language):** Defines database structure (CREATE, ALTER, DROP, TRUNCATE)
- **DML (Data Manipulation Language):** Manipulates data (SELECT, INSERT, UPDATE, DELETE)

**Q3: What is a Primary Key?**
**A:** A column or set of columns that uniquely identifies each row in a table. It cannot contain NULL values and must be unique.

**Q4: What is a Foreign Key?**
**A:** A column that creates a relationship between two tables by referencing the primary key of another table.

**Q5: What is normalization?**
**A:** Process of organizing data to reduce redundancy and improve data integrity. Forms: 1NF, 2NF, 3NF, BCNF.

**Q6: Difference between DELETE, TRUNCATE, and DROP?**
**A:**
- **DELETE:** Removes rows one by one, can use WHERE, can rollback, slower
- **TRUNCATE:** Removes all rows at once, cannot rollback, faster
- **DROP:** Deletes entire table structure

---

### **SQL Queries**

**Q7: What is the difference between WHERE and HAVING?**
**A:**
- **WHERE:** Filters rows before grouping
- **HAVING:** Filters groups after GROUP BY clause

**Q8: What are aggregate functions?**
**A:** Functions that perform calculations on multiple rows: COUNT(), SUM(), AVG(), MAX(), MIN()

**Q9: What is a View?**
**A:** Virtual table based on a SELECT query. It doesn't store data but provides a way to simplify complex queries.

**Q10: Difference between INNER JOIN and OUTER JOIN?**
**A:**
- **INNER JOIN:** Returns only matching records from both tables
- **OUTER JOIN:** Returns matching + non-matching records (LEFT/RIGHT/FULL)

**Q11: What is a subquery?**
**A:** A query nested inside another query. Used in WHERE, FROM, or SELECT clauses.

**Q12: What is an Index?**
**A:** Database object that improves query performance by creating a pointer to data locations.

---

### **MongoDB**

**Q13: What is MongoDB?**
**A:** NoSQL document-oriented database that stores data in JSON-like documents (BSON format).

**Q14: Difference between SQL and NoSQL?**
**A:**
- **SQL:** Structured, table-based, ACID properties, vertical scaling
- **NoSQL:** Unstructured/semi-structured, document/key-value, horizontal scaling

**Q15: What is a Collection in MongoDB?**
**A:** Group of documents, equivalent to a table in RDBMS.

**Q16: What is a Document in MongoDB?**
**A:** Set of key-value pairs with dynamic schema, equivalent to a row in RDBMS.

**Q17: What are CRUD operations?**
**A:** Create (insert), Read (find), Update (update), Delete (remove)

---

### **PL/SQL**

**Q18: What is PL/SQL?**
**A:** Procedural Language extension of SQL that adds programming constructs like loops, conditions, and exception handling.

**Q19: What is the structure of a PL/SQL block?**
**A:** DECLARE (optional), BEGIN (mandatory), EXCEPTION (optional), END (mandatory)

**Q20: What is an Exception?**
**A:** Runtime error in PL/SQL. Can be predefined (NO_DATA_FOUND) or user-defined.

**Q21: What is a Cursor?**
**A:** Database object to retrieve and process rows from a query result set, one row at a time.

**Q22: Difference between Implicit and Explicit Cursor?**
**A:**
- **Implicit:** Automatically created by Oracle for DML statements
- **Explicit:** User-defined in DECLARE section for SELECT queries

**Q23: What are cursor attributes?**
**A:** %FOUND, %NOTFOUND, %ISOPEN, %ROWCOUNT

**Q24: What is a Parameterized Cursor?**
**A:** Cursor that accepts parameters to filter results dynamically.

---

### **Database Connectivity**

**Q25: What is JDBC?**
**A:** Java Database Connectivity - API for connecting Java applications to databases.

**Q26: Steps to connect Java with MySQL?**
**A:**
1. Load Driver (Class.forName)
2. Create Connection (DriverManager.getConnection)
3. Create Statement
4. Execute Query
5. Close Connection

**Q27: What is a ResultSet?**
**A:** Object that holds data retrieved from database after executing a query.

**Q28: Difference between Statement and PreparedStatement?**
**A:**
- **Statement:** Used for static queries, slower, SQL injection risk
- **PreparedStatement:** Precompiled, faster, prevents SQL injection

---

## 🎓 **Quick Tips for Practical Exam**

### **Before the Exam:**
1. ✅ Practice all 6 experiments at least twice
2. ✅ Remember basic syntax (don't need to memorize everything)
3. ✅ Understand the logic behind each query
4. ✅ Know how to handle common errors

### **During the Exam:**
1. ✅ Read the problem statement carefully
2. ✅ Plan your approach before coding
3. ✅ Write clean, indented code
4. ✅ Test your queries/programs
5. ✅ Handle exceptions properly
6. ✅ Comment your code for clarity

### **Common Mistakes to Avoid:**
1. ❌ Forgetting semicolons
2. ❌ Case sensitivity in identifiers
3. ❌ Not handling exceptions in PL/SQL
4. ❌ Forgetting to commit transactions
5. ❌ Not closing cursors/connections

---

## 📚 **Important Commands Cheat Sheet**

### **MySQL/Oracle:**
```sql
-- Show databases
SHOW DATABASES;

-- Use database
USE database_name;

-- Show tables
SHOW TABLES;

-- Describe table structure
DESC table_name;

-- Enable output in PL/SQL
SET SERVEROUTPUT ON;
```

### **MongoDB:**
```javascript
// Show databases
show dbs

// Show collections
show collections

// Drop database
db.dropDatabase()

// Drop collection
db.collection_name.drop()
```

---

## 🚀 **Final Preparation Checklist**

- [ ] Can create tables with all constraints
- [ ] Can write SELECT queries with WHERE, ORDER BY, GROUP BY
- [ ] Understand all types of JOINs
- [ ] Can write subqueries
- [ ] Know MongoDB CRUD operations
- [ ] Can use logical operators in MongoDB
- [ ] Can write PL/SQL blocks with proper structure
- [ ] Know all control structures (IF, LOOP, FOR, WHILE)
- [ ] Can handle exceptions (predefined and user-defined)
- [ ] Understand cursor types and can implement them
- [ ] Know JDBC connection steps

---

**Good luck with your mock practical! 🎯**

Focus on understanding concepts rather than memorizing. Practice the code patterns, and you'll do great!