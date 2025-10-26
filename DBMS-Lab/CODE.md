# Complete Code for All 6 DBMS Experiments

## 📌 **Experiment 1: SQL DDL & DML Commands**

### Problem Statement: Bank Database System

```sql
-- ============================================
-- EXPERIMENT 1: SQL DDL & DML COMMANDS
-- ============================================

-- Create Database
CREATE DATABASE bank_db;
USE bank_db;

-- 1. Create Branch Table
CREATE TABLE branch (
    branch_name VARCHAR(50) PRIMARY KEY,
    branch_city VARCHAR(50) NOT NULL,
    assets DECIMAL(15,2) CHECK (assets >= 0)
);

-- 2. Create Account Table
CREATE TABLE account (
    acc_no INT PRIMARY KEY,
    branch_name VARCHAR(50),
    balance DECIMAL(10,2) CHECK (balance >= 0),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

-- 3. Create Customer Table
CREATE TABLE customer (
    cust_name VARCHAR(50) PRIMARY KEY,
    cust_street VARCHAR(100),
    cust_city VARCHAR(50)
);

-- 4. Create Depositor Table
CREATE TABLE depositor (
    cust_name VARCHAR(50),
    acc_no INT,
    PRIMARY KEY (cust_name, acc_no),
    FOREIGN KEY (cust_name) REFERENCES customer(cust_name),
    FOREIGN KEY (acc_no) REFERENCES account(acc_no)
);

-- 5. Create Loan Table
CREATE TABLE loan (
    loan_no INT PRIMARY KEY,
    branch_name VARCHAR(50),
    amount DECIMAL(10,2) CHECK (amount > 0),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

-- 6. Create Borrower Table
CREATE TABLE borrower (
    cust_name VARCHAR(50),
    loan_no INT,
    PRIMARY KEY (cust_name, loan_no),
    FOREIGN KEY (cust_name) REFERENCES customer(cust_name),
    FOREIGN KEY (loan_no) REFERENCES loan(loan_no)
);

-- ============================================
-- INSERT SAMPLE DATA
-- ============================================

-- Insert into Branch
INSERT INTO branch VALUES ('Akurdi', 'Pune', 5000000);
INSERT INTO branch VALUES ('Nigdi', 'Pune', 3000000);
INSERT INTO branch VALUES ('Pimpri', 'Pune', 4500000);
INSERT INTO branch VALUES ('Chinchwad', 'Pune', 6000000);

-- Insert into Customer
INSERT INTO customer VALUES ('Amit', 'MG Road', 'Pune');
INSERT INTO customer VALUES ('Priya', 'FC Road', 'Pune');
INSERT INTO customer VALUES ('Rahul', 'JM Road', 'Mumbai');
INSERT INTO customer VALUES ('Sneha', 'Camp Area', 'Pune');
INSERT INTO customer VALUES ('Vijay', 'Karve Road', 'Pune');

-- Insert into Account
INSERT INTO account VALUES (101, 'Akurdi', 15000);
INSERT INTO account VALUES (102, 'Akurdi', 8000);
INSERT INTO account VALUES (103, 'Nigdi', 20000);
INSERT INTO account VALUES (104, 'Pimpri', 12000);
INSERT INTO account VALUES (105, 'Akurdi', 25000);

-- Insert into Depositor
INSERT INTO depositor VALUES ('Amit', 101);
INSERT INTO depositor VALUES ('Priya', 102);
INSERT INTO depositor VALUES ('Rahul', 103);
INSERT INTO depositor VALUES ('Sneha', 104);
INSERT INTO depositor VALUES ('Vijay', 105);

-- Insert into Loan
INSERT INTO loan VALUES (201, 'Akurdi', 15000);
INSERT INTO loan VALUES (202, 'Akurdi', 10000);
INSERT INTO loan VALUES (203, 'Nigdi', 1400);
INSERT INTO loan VALUES (204, 'Pimpri', 8000);
INSERT INTO loan VALUES (205, 'Nigdi', 1350);

-- Insert into Borrower
INSERT INTO borrower VALUES ('Amit', 201);
INSERT INTO borrower VALUES ('Priya', 202);
INSERT INTO borrower VALUES ('Rahul', 203);
INSERT INTO borrower VALUES ('Vijay', 204);

-- ============================================
-- QUERIES (Minimum 10 queries required)
-- ============================================

-- Q1. Find the names of all branches in loan relation
SELECT DISTINCT branch_name 
FROM loan;

-- Q2. Find all loan numbers for loans made at Akurdi Branch with loan amount > 12000
SELECT loan_no 
FROM loan 
WHERE branch_name = 'Akurdi' AND amount > 12000;

-- Q3. Find all customers who have a loan from bank. Find their names, loan_no and loan amount
SELECT c.cust_name, b.loan_no, l.amount
FROM customer c
INNER JOIN borrower b ON c.cust_name = b.cust_name
INNER JOIN loan l ON b.loan_no = l.loan_no;

-- Q4. List all customers in alphabetical order who have loan from Akurdi branch
SELECT DISTINCT c.cust_name
FROM customer c
INNER JOIN borrower b ON c.cust_name = b.cust_name
INNER JOIN loan l ON b.loan_no = l.loan_no
WHERE l.branch_name = 'Akurdi'
ORDER BY c.cust_name ASC;

-- Q5. Find all customers who have an account or loan or both at bank
SELECT DISTINCT cust_name FROM depositor
UNION
SELECT DISTINCT cust_name FROM borrower;

-- Q6. Find all customers who have both account and loan at bank
SELECT DISTINCT d.cust_name
FROM depositor d
INNER JOIN borrower b ON d.cust_name = b.cust_name;

-- Q7. Find all customers who have account but no loan at the bank
SELECT DISTINCT cust_name FROM depositor
EXCEPT
SELECT DISTINCT cust_name FROM borrower;

-- Alternative for MySQL (doesn't support EXCEPT)
SELECT DISTINCT d.cust_name
FROM depositor d
WHERE d.cust_name NOT IN (SELECT cust_name FROM borrower);

-- Q8. Find average account balance at Akurdi branch
SELECT AVG(a.balance) AS avg_balance
FROM account a
WHERE a.branch_name = 'Akurdi';

-- Q9. Find the average account balance at each branch
SELECT branch_name, AVG(balance) AS avg_balance
FROM account
GROUP BY branch_name;

-- Q10. Find no. of depositors at each branch
SELECT a.branch_name, COUNT(d.cust_name) AS num_depositors
FROM account a
INNER JOIN depositor d ON a.acc_no = d.acc_no
GROUP BY a.branch_name;

-- Q11. Find the branches where average account balance > 12000
SELECT branch_name
FROM account
GROUP BY branch_name
HAVING AVG(balance) > 12000;

-- Q12. Find number of tuples in customer relation
SELECT COUNT(*) AS total_customers
FROM customer;

-- Q13. Calculate total loan amount given by bank
SELECT SUM(amount) AS total_loan_amount
FROM loan;

-- Q14. Delete all loans with loan amount between 1300 and 1500
DELETE FROM borrower WHERE loan_no IN 
    (SELECT loan_no FROM loan WHERE amount BETWEEN 1300 AND 1500);
DELETE FROM loan WHERE amount BETWEEN 1300 AND 1500;

-- Q15. Delete all tuples at every branch located in Nigdi
-- First delete dependent records
DELETE FROM depositor WHERE acc_no IN 
    (SELECT acc_no FROM account WHERE branch_name = 'Nigdi');
DELETE FROM borrower WHERE loan_no IN 
    (SELECT loan_no FROM loan WHERE branch_name = 'Nigdi');
DELETE FROM account WHERE branch_name = 'Nigdi';
DELETE FROM loan WHERE branch_name = 'Nigdi';
DELETE FROM branch WHERE branch_name = 'Nigdi';

-- Q16. Create synonym for customer table as cust (Use View as alternative)
CREATE VIEW cust AS SELECT * FROM customer;

-- Q17. Create sequence and use in student table (AUTO_INCREMENT alternative)
CREATE TABLE student (
    roll_no INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    dept VARCHAR(50)
);

-- ============================================
-- CREATE INDEX
-- ============================================
CREATE INDEX idx_branch ON account(branch_name);
CREATE INDEX idx_amount ON loan(amount);

-- ============================================
-- UPDATE OPERATIONS
-- ============================================
-- Update balance for specific account
UPDATE account 
SET balance = balance + 1000 
WHERE acc_no = 101;

-- Update all accounts in Akurdi branch
UPDATE account 
SET balance = balance * 1.05 
WHERE branch_name = 'Akurdi';

-- ============================================
-- VIEW OPERATIONS
-- ============================================
-- Create view for high balance accounts
CREATE VIEW high_balance_accounts AS
SELECT a.acc_no, a.branch_name, a.balance, c.cust_name
FROM account a
INNER JOIN depositor d ON a.acc_no = d.acc_no
INNER JOIN customer c ON d.cust_name = c.cust_name
WHERE a.balance > 10000;

-- Query the view
SELECT * FROM high_balance_accounts;

-- Update view (modifies base table)
CREATE OR REPLACE VIEW high_balance_accounts AS
SELECT a.acc_no, a.branch_name, a.balance, c.cust_name, c.cust_city
FROM account a
INNER JOIN depositor d ON a.acc_no = d.acc_no
INNER JOIN customer c ON d.cust_name = c.cust_name
WHERE a.balance > 10000;
```

---

## 📌 **Experiment 2: SQL Joins, Sub-Queries & Views**

```sql
-- ============================================
-- EXPERIMENT 2: JOINS, SUB-QUERIES & VIEWS
-- ============================================

USE bank_db;

-- ============================================
-- PROBLEM 1: Customer Address Retrieval
-- ============================================

-- Create Tables
CREATE TABLE customer_master (
    cust_no INT PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50)
);

CREATE TABLE address_details (
    cust_no INT,
    add1 VARCHAR(100),
    add2 VARCHAR(100),
    state VARCHAR(50),
    city VARCHAR(50),
    pincode VARCHAR(10),
    FOREIGN KEY (cust_no) REFERENCES customer_master(cust_no)
);

-- Insert Data
INSERT INTO customer_master VALUES (1, 'xyz', 'pqr');
INSERT INTO customer_master VALUES (2, 'John', 'Doe');
INSERT INTO customer_master VALUES (3, 'Alice', 'Smith');

INSERT INTO address_details VALUES (1, 'Lane 1', 'Kothrud', 'Maharashtra', 'Pune', '411038');
INSERT INTO address_details VALUES (2, 'Street 5', 'Viman Nagar', 'Maharashtra', 'Pune', '411014');
INSERT INTO address_details VALUES (3, 'Road 10', 'Hinjewadi', 'Maharashtra', 'Pune', '411057');

-- Query: Retrieve address of customer with fname='xyz' and lname='pqr'
SELECT cm.cust_no, cm.fname, cm.lname, ad.add1, ad.add2, ad.city, ad.state, ad.pincode
FROM customer_master cm
INNER JOIN address_details ad ON cm.cust_no = ad.cust_no
WHERE cm.fname = 'xyz' AND cm.lname = 'pqr';

-- ============================================
-- PROBLEM 2: Fixed Deposit Customers
-- ============================================

CREATE TABLE acc_fd_cust_details (
    cust_no INT,
    acc_fd_no INT,
    PRIMARY KEY (cust_no, acc_fd_no)
);

CREATE TABLE fd_details (
    fd_sr_no INT PRIMARY KEY,
    acc_fd_no INT,
    amt DECIMAL(10,2)
);

-- Insert Data
INSERT INTO acc_fd_cust_details VALUES (1, 1001);
INSERT INTO acc_fd_cust_details VALUES (2, 1002);
INSERT INTO acc_fd_cust_details VALUES (3, 1003);

INSERT INTO fd_details VALUES (1, 1001, 6000);
INSERT INTO fd_details VALUES (2, 1002, 3000);
INSERT INTO fd_details VALUES (3, 1003, 8000);

-- Query: List customers with FD > 5000
SELECT cm.cust_no, cm.fname, cm.lname, fd.amt
FROM customer_master cm
INNER JOIN acc_fd_cust_details afc ON cm.cust_no = afc.cust_no
INNER JOIN fd_details fd ON afc.acc_fd_no = fd.acc_fd_no
WHERE fd.amt > 5000;

-- ============================================
-- PROBLEM 3: Employee and Branch Details
-- ============================================

CREATE TABLE emp_master (
    emp_no INT PRIMARY KEY,
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    m_name VARCHAR(50),
    dept VARCHAR(50),
    desg VARCHAR(50),
    branch_no INT
);

CREATE TABLE branch_master (
    branch_no INT PRIMARY KEY,
    branch_name VARCHAR(50)
);

-- Insert Data
INSERT INTO branch_master VALUES (1, 'Pune Branch');
INSERT INTO branch_master VALUES (2, 'Mumbai Branch');
INSERT INTO branch_master VALUES (3, 'Delhi Branch');

INSERT INTO emp_master VALUES (101, 'Raj', 'Kumar', 'Singh', 'IT', 'Manager', 1);
INSERT INTO emp_master VALUES (102, 'Priya', 'Sharma', 'K', 'HR', 'Executive', 2);
INSERT INTO emp_master VALUES (103, 'Amit', 'Patel', 'R', 'Finance', 'Analyst', 1);

-- Query: List employee details with branch names
SELECT e.emp_no, e.f_name, e.l_name, e.dept, e.desg, b.branch_name
FROM emp_master e
INNER JOIN branch_master b ON e.branch_no = b.branch_no;

-- ============================================
-- PROBLEM 4: Employee Contact Details (LEFT & RIGHT JOIN)
-- ============================================

CREATE TABLE contact_details (
    emp_no INT,
    cntc_type VARCHAR(20),
    cntc_data VARCHAR(50),
    FOREIGN KEY (emp_no) REFERENCES emp_master(emp_no)
);

-- Insert Data
INSERT INTO contact_details VALUES (101, 'Mobile', '9876543210');
INSERT INTO contact_details VALUES (101, 'Email', 'raj@email.com');
INSERT INTO contact_details VALUES (102, 'Mobile', '8765432109');
-- Note: emp_no 103 has no contact details

-- LEFT OUTER JOIN (All employees, even without contacts)
SELECT e.emp_no, e.f_name, e.l_name, c.cntc_type, c.cntc_data
FROM emp_master e
LEFT OUTER JOIN contact_details c ON e.emp_no = c.emp_no;

-- RIGHT OUTER JOIN (All contacts, even if employee doesn't exist)
SELECT e.emp_no, e.f_name, e.l_name, c.cntc_type, c.cntc_data
FROM emp_master e
RIGHT OUTER JOIN contact_details c ON e.emp_no = c.emp_no;

-- ============================================
-- PROBLEM 5: Customers Without Nearby Branches
-- ============================================

CREATE TABLE cust_branch (
    cust_no INT PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50),
    branch_no INT
);

CREATE TABLE address_with_pin (
    cust_no INT,
    pincode VARCHAR(10),
    FOREIGN KEY (cust_no) REFERENCES cust_branch(cust_no)
);

CREATE TABLE branch_pin (
    branch_no INT PRIMARY KEY,
    branch_name VARCHAR(50),
    pincode VARCHAR(10)
);

-- Insert Data
INSERT INTO cust_branch VALUES (1, 'Amit', 'Kumar', 1);
INSERT INTO cust_branch VALUES (2, 'Priya', 'Singh', 2);
INSERT INTO cust_branch VALUES (3, 'Rahul', 'Patil', 3);

INSERT INTO address_with_pin VALUES (1, '411038');
INSERT INTO address_with_pin VALUES (2, '411014');
INSERT INTO address_with_pin VALUES (3, '411057');

INSERT INTO branch_pin VALUES (1, 'Kothrud Branch', '411038');
INSERT INTO branch_pin VALUES (2, 'Viman Nagar Branch', '411015'); -- Different pincode

-- Query: Customers without branches in their vicinity
SELECT c.cust_no, c.fname, c.lname, a.pincode
FROM cust_branch c
INNER JOIN address_with_pin a ON c.cust_no = a.cust_no
WHERE a.pincode NOT IN (SELECT pincode FROM branch_pin);

-- ============================================
-- SUB-QUERY EXAMPLES
-- ============================================

-- 1. Single-row subquery: Find customers with balance > average
SELECT cust_name
FROM customer c
INNER JOIN depositor d ON c.cust_name = d.cust_name
INNER JOIN account a ON d.acc_no = a.acc_no
WHERE a.balance > (SELECT AVG(balance) FROM account);

-- 2. Multi-row subquery with IN
SELECT cust_name
FROM customer
WHERE cust_name IN (
    SELECT cust_name FROM borrower
    WHERE loan_no IN (SELECT loan_no FROM loan WHERE amount > 10000)
);

-- 3. Correlated subquery
SELECT c.cust_name, a.balance
FROM customer c
INNER JOIN depositor d ON c.cust_name = d.cust_name
INNER JOIN account a ON d.acc_no = a.acc_no
WHERE a.balance > (
    SELECT AVG(balance) 
    FROM account a2 
    WHERE a2.branch_name = a.branch_name
);

-- 4. EXISTS subquery
SELECT c.cust_name
FROM customer c
WHERE EXISTS (
    SELECT 1 FROM borrower b WHERE b.cust_name = c.cust_name
);

-- 5. NOT EXISTS subquery
SELECT c.cust_name
FROM customer c
WHERE NOT EXISTS (
    SELECT 1 FROM borrower b WHERE b.cust_name = c.cust_name
);

-- ============================================
-- VIEW OPERATIONS
-- ============================================

-- Create view on borrower table
CREATE VIEW borrower_view AS
SELECT cust_name, loan_no FROM borrower;

-- Insert through view
INSERT INTO borrower_view VALUES ('Sneha', 205);

-- Update through view
UPDATE borrower_view SET loan_no = 206 WHERE cust_name = 'Sneha';

-- Delete through view
DELETE FROM borrower_view WHERE cust_name = 'Sneha';

-- Create view joining borrower and depositor
CREATE VIEW cust_details_view AS
SELECT b.cust_name, b.loan_no
FROM borrower b;

-- Complex view with JOIN
CREATE VIEW customer_full_details AS
SELECT c.cust_name, c.cust_city, a.acc_no, a.balance, l.loan_no, l.amount
FROM customer c
LEFT JOIN depositor d ON c.cust_name = d.cust_name
LEFT JOIN account a ON d.acc_no = a.acc_no
LEFT JOIN borrower b ON c.cust_name = b.cust_name
LEFT JOIN loan l ON b.loan_no = l.loan_no;

SELECT * FROM customer_full_details;
```

---

## 📌 **Experiment 3: MongoDB CRUD Operations**

```javascript
// ============================================
// EXPERIMENT 3: MongoDB CRUD OPERATIONS
// ============================================

// 1. Create Database
use DYPCOE

// 2. Create Collections
db.createCollection("Teachers")
db.createCollection("Students")

// ============================================
// INSERT OPERATIONS (CREATE)
// ============================================

// 3. Insert Teachers data
db.Teachers.insertMany([
    {
        Tname: "Praveen",
        dno: 1,
        dname: "Computer",
        experience: 5,
        salary: 50000,
        date_of_joining: new Date("2018-07-15")
    },
    {
        Tname: "Amit",
        dno: 1,
        dname: "Computer",
        experience: 8,
        salary: 60000,
        date_of_joining: new Date("2015-08-20")
    },
    {
        Tname: "Priya",
        dno: 2,
        dname: "IT",
        experience: 6,
        salary: 55000,
        date_of_joining: new Date("2017-06-10")
    },
    {
        Tname: "Rahul",
        dno: 3,
        dname: "E&TC",
        experience: 4,
        salary: 45000,
        date_of_joining: new Date("2019-09-01")
    },
    {
        Tname: "Sneha",
        dno: 2,
        dname: "IT",
        experience: 7,
        salary: 58000,
        date_of_joining: new Date("2016-05-12")
    },
    {
        Tname: "Vikram",
        dno: 1,
        dname: "Computer",
        experience: 3,
        salary: 42000,
        date_of_joining: new Date("2020-01-15")
    }
])

// Insert Students data
db.Students.insertMany([
    { Sname: "John", roll_no: 1, class: "TE" },
    { Sname: "Alice", roll_no: 2, class: "SE" },
    { Sname: "xyz", roll_no: 3, class: "BE" },
    { Sname: "Bob", roll_no: 4, class: "TE" },
    { Sname: "Emma", roll_no: 5, class: "SE" }
])

// ============================================
// READ OPERATIONS (FIND)
// ============================================

// 3. Find information about all teachers
db.Teachers.find().pretty()

// 4. Find teachers of Computer department
db.Teachers.find({ dname: "Computer" }).pretty()

// 5. Find teachers of Computer, IT, and E&TC department
db.Teachers.find({
    dname: { $in: ["Computer", "IT", "E&TC"] }
}).pretty()

// 6. Find teachers of Computer, IT, E&TC with salary >= 10000
db.Teachers.find({
    dname: { $in: ["Computer", "IT", "E&TC"] },
    salary: { $gte: 10000 }
}).pretty()

// 7. Find student with roll_no=2 OR Sname=xyz
db.Students.find({
    $or: [
        { roll_no: 2 },
        { Sname: "xyz" }
    ]
}).pretty()

// 10. Find teacher names and their experience only
db.Teachers.find(
    {},
    { Tname: 1, experience: 1, _id: 0 }
).pretty()

// Additional READ queries
db.Teachers.find({ salary: { $gt: 50000 } }).pretty()
db.Teachers.find({ experience: { $lte: 5 } }).pretty()
db.Teachers.findOne({ Tname: "Praveen" })

// ============================================
// UPDATE OPERATIONS
// ============================================

// 8. Update experience of teacher Praveen to 10 years (using save)
var teacher = db.Teachers.findOne({ Tname: "Praveen" })
if (teacher) {
    teacher.experience = 10
    db.Teachers.save(teacher)
} else {
    // Insert new entry if not found
    db.Teachers.save({
        Tname: "Praveen",
        dno: 1,
        dname: "Computer",
        experience: 10,
        salary: 50000,
        date_of_joining: new Date()
    })
}

// 9. Update department of all IT teachers to COMP
db.Teachers.updateMany(
    { dname: "IT" },
    { $set: { dname: "COMP" } }
)

// 11. Using save() method to insert one entry
db.Teachers.save({
    Tname: "Neha",
    dno: 4,
    dname: "Mechanical",
    experience: 5,
    salary: 48000,
    date_of_joining: new Date("2018-11-20")
})

// 12. Using save() to change dept of Praveen to IT
var praveen = db.Teachers.findOne({ Tname: "Praveen" })
praveen.dname = "IT"
db.Teachers.save(praveen)

// Update using update() method
db.Teachers.update(
    { Tname: "Amit" },
    { $set: { salary: 65000 } }
)

// Increment salary by 5000
db.Teachers.update(
    { Tname: "Priya" },
    { $inc: { salary: 5000 } }
)

// ============================================
// DELETE OPERATIONS
// ============================================

// 13. Delete all documents from Teachers with IT dept
db.Teachers.remove({ dname: "IT" })

// Delete single document
db.Teachers.remove({ Tname: "Vikram" }, { justOne: true })

// Delete all documents (use with caution!)
// db.Teachers.remove({})

// ============================================
// ADVANCED QUERIES
// ============================================

// 14. Display first 3 documents in ascending order
db.Teachers.find().sort({ Tname: 1 }).limit(3).pretty()

// Count documents
db.Teachers.count()
db.Teachers.count({ dname: "Computer" })

// Distinct values
db.Teachers.distinct("dname")

// Sort by salary descending
db.Teachers.find().sort({ salary: -1 }).pretty()

// Find and sort
db.Teachers.find({ salary: { $gte: 50000 } }).sort({ experience: -1 }).pretty()

// Logical operators - AND
db.Teachers.find({
    dname: "Computer",
    salary: { $gt: 45000 }
}).pretty()

// Logical operators - OR
db.Teachers.find({
    $or: [
        { dname: "Computer" },
        { experience: { $gt: 7 } }
    ]
}).pretty()

// Combined AND & OR
db.Teachers.find({
    salary: { $gte: 45000 },
    $or: [
        { dname: "Computer" },
        { dname: "E&TC" }
    ]
}).pretty()

// NOT operator
db.Teachers.find({
    dname: { $ne: "Computer" }
}).pretty()

// ============================================
// AGGREGATION OPERATIONS
// ============================================

// Average salary by department
db.Teachers.aggregate([
    {
        $group: {
            _id: "$dname",
            avgSalary: { $avg: "$salary" },
            count: { $sum: 1 }
        }
    }
])

// Total salary by department
db.Teachers.aggregate([
    {
        $group: {
            _id: "$dname",
            totalSalary: { $sum: "$salary" }
        }
    }
])

// Max and Min salary
db.Teachers.aggregate([
    {
        $group: {
            _id: null,
            maxSalary: { $max: "$salary" },
            minSalary: { $min: "$salary" }
        }
    }
])

// ============================================
// INDEXING
// ============================================

// Create index on Tname
db.Teachers.createIndex({ Tname: 1 })

// Create compound index
db.Teachers.createIndex({ dname: 1, salary: -1 })

// Show indexes
db.Teachers.getIndexes()

// Drop index
db.Teachers.dropIndex("Tname_1")

// ============================================
// UTILITY COMMANDS
// ============================================

// Show all collections
show collections

// Drop collection
db.Students.drop()

// Drop database
db.dropDatabase()

// Get collection stats
db.Teachers.stats()
```

---

## 📌 **Experiment 4: PL/SQL Control Structures & Exception Handling**

```sql
-- ============================================
-- EXPERIMENT 4: PL/SQL CONTROL & EXCEPTION HANDLING
-- ============================================

-- Enable output
SET SERVEROUTPUT ON;

-- ============================================
-- PROBLEM 1: Student Attendance and Term Grant
-- ============================================

-- Create Table
CREATE TABLE Stud (
    Roll INT PRIMARY KEY,
    Att NUMBER(5,2),
    Status CHAR(2)
);

-- Insert Sample Data
INSERT INTO Stud VALUES (1, 80.5, NULL);
INSERT INTO Stud VALUES (2, 65.0, NULL);
INSERT INTO Stud VALUES (3, 78.5, NULL);
INSERT INTO Stud VALUES (4, 60.0, NULL);
INSERT INTO Stud VALUES (5, 85.0, NULL);

-- PL/SQL Block
DECLARE
    v_roll Stud.Roll%TYPE;
    v_att Stud.Att%TYPE;
    v_status Stud.Status%TYPE;
BEGIN
    -- Accept roll number from user
    v_roll := &roll_no;
    
    -- Fetch attendance
    SELECT Att INTO v_att FROM Stud WHERE Roll = v_roll;
    
    -- Check attendance and set status
    IF v_att < 75 THEN
        v_status := 'D';
        DBMS_OUTPUT.PUT_LINE('Term not granted');
    ELSE
        v_status := 'ND';
        DBMS_OUTPUT.PUT_LINE('Term granted');
    END IF;
    
    -- Update status in table
    UPDATE Stud SET Status = v_status WHERE Roll = v_roll;
    COMMIT;
    
    DBMS_OUTPUT.PUT_LINE('Roll No: ' || v_roll);
    DBMS_OUTPUT.PUT_LINE('Attendance: ' || v_att || '%');
    DBMS_OUTPUT.PUT_LINE('Status: ' || v_status);
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Error: Student with Roll No ' || v_roll || ' not found!');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/

-- ============================================
-- PROBLEM 2: Bank Account Withdrawal with User-Defined Exception
-- ============================================

-- Create Table
CREATE TABLE account_master (
    acc_no INT PRIMARY KEY,
    acc_holder VARCHAR(50),
    balance DECIMAL(10,2)
);

-- Insert Sample Data
INSERT INTO account_master VALUES (101, 'Amit Kumar', 5000);
INSERT INTO account_master VALUES (102, 'Priya Singh', 15000);
INSERT INTO account_master VALUES (103, 'Rahul Patil', 8000);

-- PL/SQL Block with User-Defined Exception
DECLARE
    v_acc_no account_master.acc_no%TYPE;
    v_balance account_master.balance%TYPE;
    v_withdrawal DECIMAL(10,2);
    insufficient_balance EXCEPTION;
BEGIN
    -- Accept account number and withdrawal amount
    v_acc_no := &account_number;
    v_withdrawal := &withdrawal_amount;
    
    -- Fetch current balance
    SELECT balance INTO v_balance FROM account_master WHERE acc_no = v_acc_no;
    
    DBMS_OUTPUT.PUT_LINE('Account Number: ' || v_acc_no);
    DBMS_OUTPUT.PUT_LINE('Current Balance: ' || v_balance);
    DBMS_OUTPUT.PUT_LINE('Withdrawal Amount: ' || v_withdrawal);
    
    -- Check if withdrawal is possible
    IF v_withdrawal > v_balance THEN
        RAISE insufficient_balance;
    ELSE
        -- Process withdrawal
        UPDATE account_master 
        SET balance = balance - v_withdrawal 
        WHERE acc_no = v_acc_no;
        
        COMMIT;
        
        DBMS_OUTPUT.PUT_LINE('Withdrawal successful!');
        DBMS_OUTPUT.PUT_LINE('New Balance: ' || (v_balance - v_withdrawal));
    END IF;
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Error: Account not found!');
    WHEN insufficient_balance THEN
        DBMS_OUTPUT.PUT_LINE('Error: Insufficient balance! Cannot withdraw ' || v_withdrawal);
        DBMS_OUTPUT.PUT_LINE('Available balance: ' || v_balance);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/

-- ============================================
-- PROBLEM 3: Library Fine Calculation (Borrower System)
-- ============================================

-- Create Tables
CREATE TABLE Borrower (
    Roll_no INT PRIMARY KEY,
    Name VARCHAR(50),
    Date_of_Issue DATE,
    Name_of_Book VARCHAR(100),
    Status CHAR(1) -- 'I' for Issued, 'R' for Returned
);

CREATE TABLE Fine (
    Roll_no INT,
    Date_returned DATE,
    Amt DECIMAL(10,2)
);

-- Insert Sample Data
INSERT INTO Borrower VALUES (1, 'Amit', TO_DATE('2024-09-15', 'YYYY-MM-DD'), 'Database Systems', 'I');
INSERT INTO Borrower VALUES (2, 'Priya', TO_DATE('2024-10-01', 'YYYY-MM-DD'), 'Data Structures', 'I');
INSERT INTO Borrower VALUES (3, 'Rahul', TO_DATE('2024-08-10', 'YYYY-MM-DD'), 'Operating Systems', 'I');
INSERT INTO Borrower VALUES (4, 'Sneha', TO_DATE('2024-10-20', 'YYYY-MM-DD'), 'Computer Networks', 'I');

-- PL/SQL Block
DECLARE
    v_roll_no Borrower.Roll_no%TYPE;
    v_book_name Borrower.Name_of_Book%TYPE;
    v_issue_date Borrower.Date_of_Issue%TYPE;
    v_days_diff INT;
    v_fine_amt DECIMAL(10,2) := 0;
    book_not_issued EXCEPTION;
    book_not_found EXCEPTION;
BEGIN
    -- Accept Roll_no and Book name from user
    v_roll_no := &roll_number;
    v_book_name := '&book_name';
    
    -- Fetch book details
    SELECT Date_of_Issue INTO v_issue_date 
    FROM Borrower 
    WHERE Roll_no = v_roll_no AND Name_of_Book = v_book_name AND Status = 'I';
    
    -- Calculate days difference
    v_days_diff := TRUNC(SYSDATE - v_issue_date);
    
    DBMS_OUTPUT.PUT_LINE('Roll No: ' || v_roll_no);
    DBMS_OUTPUT.PUT_LINE('Book: ' || v_book_name);
    DBMS_OUTPUT.PUT_LINE('Issue Date: ' || v_issue_date);
    DBMS_OUTPUT.PUT_LINE('Days: ' || v_days_diff);
    
    -- Calculate fine based on days
    IF v_days_diff > 30 THEN
        -- Rs. 50 per day for days > 30 and Rs. 5 for first 30 days
        v_fine_amt := (30 * 5) + ((v_days_diff - 30) * 50);
        DBMS_OUTPUT.PUT_LINE('Fine Amount: Rs. ' || v_fine_amt);
        
        -- Insert into Fine table
        INSERT INTO Fine VALUES (v_roll_no, SYSDATE, v_fine_amt);
        
    ELSIF v_days_diff BETWEEN 15 AND 30 THEN
        -- Rs. 5 per day
        v_fine_amt := v_days_diff * 5;
        DBMS_OUTPUT.PUT_LINE('Fine Amount: Rs. ' || v_fine_amt);
        
        -- Insert into Fine table
        INSERT INTO Fine VALUES (v_roll_no, SYSDATE, v_fine_amt);
        
    ELSE
        DBMS_OUTPUT.PUT_LINE('No fine. Book returned on time.');
    END IF;
    
    -- Update status to 'R' (Returned)
    UPDATE Borrower 
    SET Status = 'R' 
    WHERE Roll_no = v_roll_no AND Name_of_Book = v_book_name;
    
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Book returned successfully!');
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Error: Book not found or already returned!');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/

-- ============================================
-- ADDITIONAL EXAMPLES: Control Structures
-- ============================================

-- Example 1: Simple IF-THEN
DECLARE
    v_salary NUMBER := 50000;
BEGIN
    IF v_salary > 40000 THEN
        DBMS_OUTPUT.PUT_LINE('High Salary');
    END IF;
END;
/

-- Example 2: IF-THEN-ELSE
DECLARE
    v_marks NUMBER := 65;
    v_grade CHAR(1);
BEGIN
    IF v_marks >= 75 THEN
        v_grade := 'A';
    ELSE
        v_grade := 'B';
    END IF;
    DBMS_OUTPUT.PUT_LINE('Grade: ' || v_grade);
END;
/

-- Example 3: IF-THEN-ELSIF
DECLARE
    v_marks NUMBER := 85;
    v_grade VARCHAR(2);
BEGIN
    IF v_marks >= 90 THEN
        v_grade := 'A+';
    ELSIF v_marks >= 75 THEN
        v_grade := 'A';
    ELSIF v_marks >= 60 THEN
        v_grade := 'B';
    ELSIF v_marks >= 50 THEN
        v_grade := 'C';
    ELSE
        v_grade := 'F';
    END IF;
    DBMS_OUTPUT.PUT_LINE('Marks: ' || v_marks || ', Grade: ' || v_grade);
END;
/

-- Example 4: CASE Statement
DECLARE
    v_day NUMBER := 3;
    v_day_name VARCHAR(10);
BEGIN
    CASE v_day
        WHEN 1 THEN v_day_name := 'Monday';
        WHEN 2 THEN v_day_name := 'Tuesday';
        WHEN 3 THEN v_day_name := 'Wednesday';
        WHEN 4 THEN v_day_name := 'Thursday';
        WHEN 5 THEN v_day_name := 'Friday';
        ELSE v_day_name := 'Weekend';
    END CASE;
    DBMS_OUTPUT.PUT_LINE('Day: ' || v_day_name);
END;
/

-- Example 5: SIMPLE LOOP
DECLARE
    v_counter NUMBER := 1;
BEGIN
    LOOP
        DBMS_OUTPUT.PUT_LINE('Counter: ' || v_counter);
        v_counter := v_counter + 1;
        EXIT WHEN v_counter > 5;
    END LOOP;
END;
/

-- Example 6: WHILE LOOP
DECLARE
    v_counter NUMBER := 1;
BEGIN
    WHILE v_counter <= 5 LOOP
        DBMS_OUTPUT.PUT_LINE('Counter: ' || v_counter);
        v_counter := v_counter + 1;
    END LOOP;
END;
/

-- Example 7: FOR LOOP
BEGIN
    FOR i IN 1..5 LOOP
        DBMS_OUTPUT.PUT_LINE('Iteration: ' || i);
    END LOOP;
END;
/

-- Example 8: FOR LOOP with REVERSE
BEGIN
    FOR i IN REVERSE 1..5 LOOP
        DBMS_OUTPUT.PUT_LINE('Countdown: ' || i);
    END LOOP;
END;
/

-- Example 9: Nested Loops
BEGIN
    FOR i IN 1..3 LOOP
        FOR j IN 1..3 LOOP
            DBMS_OUTPUT.PUT_LINE('i=' || i || ', j=' || j);
        END LOOP;
    END LOOP;
END;
/

-- Example 10: Multiple Exception Handling
DECLARE
    v_num1 NUMBER := 10;
    v_num2 NUMBER := 0;
    v_result NUMBER;
BEGIN
    v_result := v_num1 / v_num2;
EXCEPTION
    WHEN ZERO_DIVIDE THEN
        DBMS_OUTPUT.PUT_LINE('Error: Cannot divide by zero!');
    WHEN VALUE_ERROR THEN
        DBMS_OUTPUT.PUT_LINE('Error: Invalid value!');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/
```

---

## 📌 **Experiment 5: PL/SQL Cursors**

```sql
-- ============================================
-- EXPERIMENT 5: PL/SQL CURSORS
-- ============================================

SET SERVEROUTPUT ON;

-- ============================================
-- PROBLEM 1: Implicit Cursor - Account Activation
-- ============================================

-- Create Table
CREATE TABLE accounts (
    acc_no INT PRIMARY KEY,
    acc_holder VARCHAR(50),
    status VARCHAR(10),
    last_transaction_date DATE
);

-- Insert Sample Data
INSERT INTO accounts VALUES (101, 'Amit', 'Inactive', TO_DATE('2023-01-15', 'YYYY-MM-DD'));
INSERT INTO accounts VALUES (102, 'Priya', 'Active', TO_DATE('2024-10-20', 'YYYY-MM-DD'));
INSERT INTO accounts VALUES (103, 'Rahul', 'Inactive', TO_DATE('2023-05-10', 'YYYY-MM-DD'));
INSERT INTO accounts VALUES (104, 'Sneha', 'Inactive', TO_DATE('2023-08-25', 'YYYY-MM-DD'));
INSERT INTO accounts VALUES (105, 'Vikram', 'Active', TO_DATE('2024-09-30', 'YYYY-MM-DD'));

-- PL/SQL Block with Implicit Cursor
DECLARE
    v_rows_affected NUMBER;
BEGIN
    -- Update all inactive accounts to active
    UPDATE accounts 
    SET status = 'Active' 
    WHERE status = 'Inactive';
    
    -- Check implicit cursor attributes
    IF SQL%FOUND THEN
        v_rows_affected := SQL%ROWCOUNT;
        DBMS_OUTPUT.PUT_LINE('Success: ' || v_rows_affected || ' account(s) activated.');
        
        IF v_rows_affected = 1 THEN
            DBMS_OUTPUT.PUT_LINE('Message: One account was activated.');
        ELSIF v_rows_affected BETWEEN 2 AND 5 THEN
            DBMS_OUTPUT.PUT_LINE('Message: Multiple accounts were activated.');
        ELSE
            DBMS_OUTPUT.PUT_LINE('Message: Many accounts were activated.');
        END IF;
    ELSE
        DBMS_OUTPUT.PUT_LINE('No inactive accounts found.');
    END IF;
    
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/

-- ============================================
-- PROBLEM 2: Explicit Cursor - Salary Increment
-- ============================================

-- Create Tables
CREATE TABLE EMP (
    E_no INT PRIMARY KEY,
    E_name VARCHAR(50),
    Salary DECIMAL(10,2)
);

CREATE TABLE increment_salary (
    E_no INT,
    Old_Salary DECIMAL(10,2),
    New_Salary DECIMAL(10,2),
    Increment_Date DATE
);

-- Insert Sample Data
INSERT INTO EMP VALUES (1, 'Amit', 25000);
INSERT INTO EMP VALUES (2, 'Priya', 45000);
INSERT INTO EMP VALUES (3, 'Rahul', 30000);
INSERT INTO EMP VALUES (4, 'Sneha', 35000);
INSERT INTO EMP VALUES (5, 'Vikram', 50000);

-- PL/SQL Block with Explicit Cursor
DECLARE
    CURSOR emp_cursor IS 
        SELECT E_no, E_name, Salary 
        FROM EMP 
        WHERE Salary < (SELECT AVG(Salary) FROM EMP);
    
    v_emp_no EMP.E_no%TYPE;
    v_emp_name EMP.E_name%TYPE;
    v_old_salary EMP.Salary%TYPE;
    v_new_salary EMP.Salary%TYPE;
    v_avg_salary EMP.Salary%TYPE;
BEGIN
    -- Calculate average salary
    SELECT AVG(Salary) INTO v_avg_salary FROM EMP;
    DBMS_OUTPUT.PUT_LINE('Average Salary: ' || v_avg_salary);
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    
    -- Open cursor
    OPEN emp_cursor;
    
    LOOP
        -- Fetch data
        FETCH emp_cursor INTO v_emp_no, v_emp_name, v_old_salary;
        EXIT WHEN emp_cursor%NOTFOUND;
        
        -- Calculate new salary (10% increment)
        v_new_salary := v_old_salary * 1.10;
        
        -- Display information
        DBMS_OUTPUT.PUT_LINE('Employee: ' || v_emp_name);
        DBMS_OUTPUT.PUT_LINE('Old Salary: ' || v_old_salary);
        DBMS_OUTPUT.PUT_LINE('New Salary: ' || v_new_salary);
        DBMS_OUTPUT.PUT_LINE('-----------------------------------');
        
        -- Update employee salary
        UPDATE EMP SET Salary = v_new_salary WHERE E_no = v_emp_no;
        
        -- Insert record into increment_salary table
        INSERT INTO increment_salary VALUES (v_emp_no, v_old_salary, v_new_salary, SYSDATE);
    END LOOP;
    
    -- Display cursor statistics
    DBMS_OUTPUT.PUT_LINE('Total employees processed: ' || emp_cursor%ROWCOUNT);
    
    -- Close cursor
    CLOSE emp_cursor;
    
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        IF emp_cursor%ISOPEN THEN
            CLOSE emp_cursor;
        END IF;
        ROLLBACK;
END;
/

-- ============================================
-- PROBLEM 3: Explicit Cursor with WHILE Loop - Student Detention
-- ============================================

-- Create Tables
CREATE TABLE stud21 (
    roll NUMBER(4) PRIMARY KEY,
    att NUMBER(4),
    status VARCHAR(1)
);

CREATE TABLE d_stud (
    roll NUMBER(4),
    att NUMBER(4),
    detention_date DATE
);

-- Insert Sample Data
INSERT INTO stud21 VALUES (1, 80, NULL);
INSERT INTO stud21 VALUES (2, 65, NULL);
INSERT INTO stud21 VALUES (3, 78, NULL);
INSERT INTO stud21 VALUES (4, 70, NULL);
INSERT INTO stud21 VALUES (5, 85, NULL);

-- PL/SQL Block with WHILE Loop
DECLARE
    CURSOR stud_cursor IS 
        SELECT roll, att FROM stud21 WHERE att < 75;
    
    v_roll stud21.roll%TYPE;
    v_att stud21.att%TYPE;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Students with attendance < 75%:');
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    
    OPEN stud_cursor;
    
    FETCH stud_cursor INTO v_roll, v_att;
    
    WHILE stud_cursor%FOUND LOOP
        DBMS_OUTPUT.PUT_LINE('Roll No: ' || v_roll || ', Attendance: ' || v_att || '%');
        
        -- Update status to 'D' (Detained)
        UPDATE stud21 SET status = 'D' WHERE roll = v_roll;
        
        -- Insert into d_stud table
        INSERT INTO d_stud VALUES (v_roll, v_att, SYSDATE);
        
        FETCH stud_cursor INTO v_roll, v_att;
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    DBMS_OUTPUT.PUT_LINE('Total students detained: ' || stud_cursor%ROWCOUNT);
    
    CLOSE stud_cursor;
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        IF stud_cursor%ISOPEN THEN
            CLOSE stud_cursor;
        END IF;
        ROLLBACK;
END;
/

-- ============================================
-- PROBLEM 4: Cursor FOR Loop - Student Detention (Simplified)
-- ============================================

-- PL/SQL Block with Cursor FOR Loop (No OPEN/FETCH/CLOSE needed)
DECLARE
    CURSOR stud_cursor IS 
        SELECT roll, att FROM stud21 WHERE att < 75;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Students with attendance < 75%:');
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    
    FOR stud_rec IN stud_cursor LOOP
        DBMS_OUTPUT.PUT_LINE('Roll No: ' || stud_rec.roll || ', Attendance: ' || stud_rec.att || '%');
        
        -- Update status to 'D'
        UPDATE stud21 SET status = 'D' WHERE roll = stud_rec.roll;
        
        -- Insert into d_stud
        INSERT INTO d_stud VALUES (stud_rec.roll, stud_rec.att, SYSDATE);
    END LOOP;
    
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    DBMS_OUTPUT.PUT_LINE('Process completed successfully!');
    
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/

-- ============================================
-- PROBLEM 5: Parameterized Cursor - Merge Roll Call Data
-- ============================================

-- Create Tables
CREATE TABLE O_RollCall (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    class VARCHAR(10)
);

CREATE TABLE N_RollCall (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    class VARCHAR(10)
);

-- Insert Sample Data
INSERT INTO O_RollCall VALUES (1, 'Amit', 'TE');
INSERT INTO O_RollCall VALUES (2, 'Priya', 'TE');
INSERT INTO O_RollCall VALUES (3, 'Rahul', 'TE');

INSERT INTO N_RollCall VALUES (2, 'Priya', 'TE');  -- Duplicate
INSERT INTO N_RollCall VALUES (4, 'Sneha', 'TE');  -- New
INSERT INTO N_RollCall VALUES (5, 'Vikram', 'TE'); -- New
INSERT INTO N_RollCall VALUES (1, 'Amit', 'TE');   -- Duplicate

-- PL/SQL Block with Parameterized Cursor
DECLARE
    CURSOR new_stud_cursor IS 
        SELECT roll_no, name, class FROM N_RollCall;
    
    CURSOR check_cursor(p_roll_no INT) IS
        SELECT roll_no FROM O_RollCall WHERE roll_no = p_roll_no;
    
    v_existing_roll O_RollCall.roll_no%TYPE;
    v_inserted_count INT := 0;
    v_skipped_count INT := 0;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Merging Roll Call Data...');
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    
    FOR new_rec IN new_stud_cursor LOOP
        -- Check if student already exists
        OPEN check_cursor(new_rec.roll_no);
        FETCH check_cursor INTO v_existing_roll;
        
        IF check_cursor%FOUND THEN
            -- Student exists, skip
            DBMS_OUTPUT.PUT_LINE('Skipped: Roll No ' || new_rec.roll_no || ' - ' || new_rec.name || ' (Already exists)');
            v_skipped_count := v_skipped_count + 1;
        ELSE
            -- Student doesn't exist, insert
            INSERT INTO O_RollCall VALUES (new_rec.roll_no, new_rec.name, new_rec.class);
            DBMS_OUTPUT.PUT_LINE('Inserted: Roll No ' || new_rec.roll_no || ' - ' || new_rec.name);
            v_inserted_count := v_inserted_count + 1;
        END IF;
        
        CLOSE check_cursor;
    END LOOP;
    
    COMMIT;
    
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    DBMS_OUTPUT.PUT_LINE('Total Inserted: ' || v_inserted_count);
    DBMS_OUTPUT.PUT_LINE('Total Skipped: ' || v_skipped_count);
    
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/

-- ============================================
-- PROBLEM 6: Parameterized Cursor - Department-wise Average Salary
-- ============================================

-- Create Tables
CREATE TABLE EMP_DEPT (
    e_no INT PRIMARY KEY,
    e_name VARCHAR(50),
    d_no INT,
    Salary DECIMAL(10,2)
);

CREATE TABLE dept_salary (
    d_no INT PRIMARY KEY,
    Avg_salary DECIMAL(10,2),
    calculation_date DATE
);

-- Insert Sample Data
INSERT INTO EMP_DEPT VALUES (1, 'Amit', 1, 45000);
INSERT INTO EMP_DEPT VALUES (2, 'Priya', 1, 50000);
INSERT INTO EMP_DEPT VALUES (3, 'Rahul', 2, 35000);
INSERT INTO EMP_DEPT VALUES (4, 'Sneha', 2, 40000);
INSERT INTO EMP_DEPT VALUES (5, 'Vikram', 3, 55000);
INSERT INTO EMP_DEPT VALUES (6, 'Neha', 3, 60000);

-- PL/SQL Block with Parameterized Cursor
DECLARE
    CURSOR dept_cursor IS 
        SELECT DISTINCT d_no FROM EMP_DEPT ORDER BY d_no;
    
    CURSOR avg_salary_cursor(p_dept_no INT) IS
        SELECT AVG(Salary) as avg_sal 
        FROM EMP_DEPT 
        WHERE d_no = p_dept_no;
    
    v_dept_no EMP_DEPT.d_no%TYPE;
    v_avg_salary DECIMAL(10,2);
BEGIN
    DBMS_OUTPUT.PUT_LINE('Department-wise Average Salary:');
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    
    FOR dept_rec IN dept_cursor LOOP
        -- Calculate average salary for each department
        OPEN avg_salary_cursor(dept_rec.d_no);
        FETCH avg_salary_cursor INTO v_avg_salary;
        CLOSE avg_salary_cursor;
        
        DBMS_OUTPUT.PUT_LINE('Department ' || dept_rec.d_no || ': Rs. ' || ROUND(v_avg_salary, 2));
        
        -- Insert or update dept_salary table
        BEGIN
            INSERT INTO dept_salary VALUES (dept_rec.d_no, v_avg_salary, SYSDATE);
        EXCEPTION
            WHEN DUP_VAL_ON_INDEX THEN
                UPDATE dept_salary 
                SET Avg_salary = v_avg_salary, calculation_date = SYSDATE 
                WHERE d_no = dept_rec.d_no;
        END;
    END LOOP;
    
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    DBMS_OUTPUT.PUT_LINE('Data saved to dept_salary table successfully!');
    
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/

-- ============================================
-- ADDITIONAL CURSOR EXAMPLES
-- ============================================

-- Example 1: Cursor with %ROWTYPE
DECLARE
    CURSOR emp_cursor IS SELECT * FROM EMP;
    emp_rec emp_cursor%ROWTYPE;
BEGIN
    OPEN emp_cursor;
    LOOP
        FETCH emp_cursor INTO emp_rec;
        EXIT WHEN emp_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(emp_rec.E_name || ': ' || emp_rec.Salary);
    END LOOP;
    CLOSE emp_cursor;
END;
/

-- Example 2: Inline Cursor FOR Loop
BEGIN
    FOR emp_rec IN (SELECT * FROM EMP WHERE Salary > 30000) LOOP
        DBMS_OUTPUT.PUT_LINE(emp_rec.E_name || ' earns ' || emp_rec.Salary);
    END LOOP;
END;
/

-- Example 3: Cursor with ORDER BY
DECLARE
    CURSOR emp_cursor IS 
        SELECT * FROM EMP ORDER BY Salary DESC;
BEGIN
    FOR emp_rec IN emp_cursor LOOP
        DBMS_OUTPUT.PUT_LINE(emp_rec.E_name || ': Rs. ' || emp_rec.Salary);
    END LOOP;
END;
/
```

---

## 📌 **Experiment 6: Database Connectivity (Java + MySQL)**

```java
// ============================================
// EXPERIMENT 6: DATABASE CONNECTIVITY
// ============================================

// File: StudentManagement.java

import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.*;

public class StudentManagement extends JFrame implements ActionListener {
    
    // GUI Components
    JFrame frame;
    JLabel lblTitle, lblRoll, lblName, lblDept;
    JTextField txtRoll, txtName, txtDept;
    JButton btnAdd, btnEdit, btnDelete, btnDisplay, btnExit;
    
    // Database Components
    Connection con;
    Statement stmt;
    ResultSet rs;
    
    // Constructor
    public StudentManagement() {
        try {
            // Initialize Frame
            frame = new JFrame("Student Management System");
            frame.setLayout(null);
            frame.setVisible(true);
            frame.setSize(700, 500);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.getContentPane().setBackground(new Color(240, 240, 240));
            
            // Title Label
            lblTitle = new JLabel("Student Management System");
            lblTitle.setBounds(150, 30, 400, 40);
            lblTitle.setForeground(Color.BLUE);
            lblTitle.setFont(new Font("Arial", Font.BOLD, 28));
            frame.add(lblTitle);
            
            // Roll Number
            lblRoll = new JLabel("Roll No:");
            lblRoll.setBounds(50, 100, 100, 30);
            lblRoll.setFont(new Font("Arial", Font.PLAIN, 16));
            frame.add(lblRoll);
            
            txtRoll = new JTextField();
            txtRoll.setBounds(200, 100, 150, 30);
            txtRoll.setFont(new Font("Arial", Font.PLAIN, 14));
            frame.add(txtRoll);
            
            // Student Name
            lblName = new JLabel("Student Name:");
            lblName.setBounds(50, 150, 150, 30);
            lblName.setFont(new Font("Arial", Font.PLAIN, 16));
            frame.add(lblName);
            
            txtName = new JTextField();
            txtName.setBounds(200, 150, 150, 30);
            txtName.setFont(new Font("Arial", Font.PLAIN, 14));
            frame.add(txtName);
            
            // Department
            lblDept = new JLabel("Department:");
            lblDept.setBounds(50, 200, 150, 30);
            lblDept.setFont(new Font("Arial", Font.PLAIN, 16));
            frame.add(lblDept);
            
            txtDept = new JTextField();
            txtDept.setBounds(200, 200, 150, 30);
            txtDept.setFont(new Font("Arial", Font.PLAIN, 14));
            frame.add(txtDept);
            
            // Buttons
            btnAdd = new JButton("ADD");
            btnAdd.setBounds(50, 300, 100, 40);
            btnAdd.setBackground(new Color(76, 175, 80));
            btnAdd.setForeground(Color.WHITE);
            btnAdd.setFont(new Font("Arial", Font.BOLD, 14));
            frame.add(btnAdd);
            btnAdd.addActionListener(this);
            
            btnEdit = new JButton("EDIT");
            btnEdit.setBounds(170, 300, 100, 40);
            btnEdit.setBackground(new Color(33, 150, 243));
            btnEdit.setForeground(Color.WHITE);
            btnEdit.setFont(new Font("Arial", Font.BOLD, 14));
            frame.add(btnEdit);
            btnEdit.addActionListener(this);
            
            btnDelete = new JButton("DELETE");
            btnDelete.setBounds(290, 300, 100, 40);
            btnDelete.setBackground(new Color(244, 67, 54));
            btnDelete.setForeground(Color.WHITE);
            btnDelete.setFont(new Font("Arial", Font.BOLD, 14));
            frame.add(btnDelete);
            btnDelete.addActionListener(this);
            
            btnDisplay = new JButton("DISPLAY");
            btnDisplay.setBounds(410, 300, 100, 40);
            btnDisplay.setBackground(new Color(255, 152, 0));
            btnDisplay.setForeground(Color.WHITE);
            btnDisplay.setFont(new Font("Arial", Font.BOLD, 14));
            frame.add(btnDisplay);
            btnDisplay.addActionListener(this);
            
            btnExit = new JButton("EXIT");
            btnExit.setBounds(530, 300, 100, 40);
            btnExit.setBackground(new Color(96, 125, 139));
            btnExit.setForeground(Color.WHITE);
            btnExit.setFont(new Font("Arial", Font.BOLD, 14));
            frame.add(btnExit);
            btnExit.addActionListener(this);
            
            // Database Connection
            Class.forName("com.mysql.cj.jdbc.Driver");
            con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/college_db", 
                "root", 
                "your_password"
            );
            stmt = con.createStatement();
            
            JOptionPane.showMessageDialog(frame, "Database Connected Successfully!");
            
        } catch (Exception e) {
            JOptionPane.showMessageDialog(frame, "Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    // Action Handler
    public void actionPerformed(ActionEvent ae) {
        try {
            // ADD Button
            if (ae.getSource() == btnAdd) {
                if (txtRoll.getText().isEmpty() || txtName.getText().isEmpty() || txtDept.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please fill all fields!");
                    return;
                }
                
                String query = "INSERT INTO students (roll_no, name, dept) VALUES (" 
                    + txtRoll.getText() + ", '" 
                    + txtName.getText() + "', '" 
                    + txtDept.getText() + "')";
                
                stmt.executeUpdate(query);
                JOptionPane.showMessageDialog(frame, "Record Added Successfully!");
                clearFields();
            }
            
            // EDIT Button
            else if (ae.getSource() == btnEdit) {
                if (txtRoll.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please enter Roll No to edit!");
                    return;
                }
                
                String query = "UPDATE students SET name='" + txtName.getText() 
                    + "', dept='" + txtDept.getText() 
                    + "' WHERE roll_no=" + txtRoll.getText();
                
                int rows = stmt.executeUpdate(query);
                if (rows > 0) {
                    JOptionPane.showMessageDialog(frame, "Record Updated Successfully!");
                } else {
                    JOptionPane.showMessageDialog(frame, "Record Not Found!");
                }
                clearFields();
            }
            
            // DELETE Button
            else if (ae.getSource() == btnDelete) {
                if (txtRoll.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please enter Roll No to delete!");
                    return;
                }
                
                int confirm = JOptionPane.showConfirmDialog(frame, 
                    "Are you sure you want to delete this record?", 
                    "Confirm Delete", 
                    JOptionPane.YES_NO_OPTION);
                
                if (confirm == JOptionPane.YES_OPTION) {
                    String query = "DELETE FROM students WHERE roll_no=" + txtRoll.getText();
                    int rows = stmt.executeUpdate(query);
                    
                    if (rows > 0) {
                        JOptionPane.showMessageDialog(frame, "Record Deleted Successfully!");
                    } else {
                        JOptionPane.showMessageDialog(frame, "Record Not Found!");
                    }
                    clearFields();
                }
            }
            
            // DISPLAY Button
            else if (ae.getSource() == btnDisplay) {
                rs = stmt.executeQuery("SELECT * FROM students ORDER BY roll_no");
                
                // Create display window
                JFrame displayFrame = new JFrame("Student Records");
                displayFrame.setSize(600, 400);
                displayFrame.setLayout(new BorderLayout());
                
                JTextArea textArea = new JTextArea();
                textArea.setFont(new Font("Monospaced", Font.PLAIN, 14));
                textArea.setEditable(false);
                
                StringBuilder sb = new StringBuilder();
                sb.append(String.format("%-10s %-20s %-15s\n", "Roll No", "Name", "Department"));
                sb.append("-------------------------------------------------------\n");
                
                int count = 0;
                while (rs.next()) {
                    sb.append(String.format("%-10s %-20s %-15s\n", 
                        rs.getInt("roll_no"), 
                        rs.getString("name"), 
                        rs.getString("dept")));
                    count++;
                }
                
                sb.append("-------------------------------------------------------\n");
                sb.append("Total Records: " + count);
                
                textArea.setText(sb.toString());
                
                JScrollPane scrollPane = new JScrollPane(textArea);
                displayFrame.add(scrollPane, BorderLayout.CENTER);
                displayFrame.setVisible(true);
            }
            
            // EXIT Button
            else if (ae.getSource() == btnExit) {
                int confirm = JOptionPane.showConfirmDialog(frame, 
                    "Are you sure you want to exit?", 
                    "Confirm Exit", 
                    JOptionPane.YES_NO_OPTION);
                
                if (confirm == JOptionPane.YES_OPTION) {
                    con.close();
                    System.exit(0);
                }
            }
            
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(frame, "Database Error: " + e.getMessage());
            e.printStackTrace();
        } catch (Exception e) {
            JOptionPane.showMessageDialog(frame, "Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    // Clear all text fields
    private void clearFields() {
        txtRoll.setText("");
        txtName.setText("");
        txtDept.setText("");
        txtRoll.requestFocus();
    }
    
    // Main Method
    public static void main(String[] args) {
        new StudentManagement();
    }
}
```

### **Alternative: Simple Console-Based JDBC Program**

```java
// File: SimpleDBConnection.java

import java.sql.*;
import java.util.Scanner;

public class SimpleDBConnection {
    
    static Connection con;
    static Statement stmt;
    static Scanner sc = new Scanner(System.in);
    
    public static void main(String[] args) {
        try {
            // 1. Load Driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver Loaded Successfully!");
            
            // 2. Create Connection
            con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/college_db",
                "root",
                "your_password"
            );
            System.out.println("Database Connected Successfully!");
            
            // 3. Create Statement
            stmt = con.createStatement();
            
            // Menu
            while (true) {
                System.out.println("\n========== STUDENT MANAGEMENT ==========");
                System.out.println("1. Add Student");
                System.out.println("2. Display All Students");
                System.out.println("3. Update Student");
                System.out.println("4. Delete Student");
                System.out.println("5. Search Student");
                System.out.println("6. Exit");
                System.out.print("Enter your choice: ");
                
                int choice = sc.nextInt();
                
                switch (choice) {
                    case 1:
                        addStudent();
                        break;
                    case 2:
                        displayStudents();
                        break;
                    case 3:
                        updateStudent();
                        break;
                    case 4:
                        deleteStudent();
                        break;
                    case 5:
                        searchStudent();
                        break;
                    case 6:
                        con.close();
                        System.out.println("Connection Closed. Goodbye!");
                        System.exit(0);
                    default:
                        System.out.println("Invalid choice!");
                }
            }
            
        } catch (ClassNotFoundException e) {
            System.out.println("Driver not found: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        }
    }
    
    // Add Student
    static void addStudent() {
        try {
            System.out.print("Enter Roll No: ");
            int roll = sc.nextInt();
            sc.nextLine(); // consume newline
            
            System.out.print("Enter Name: ");
            String name = sc.nextLine();
            
            System.out.print("Enter Department: ");
            String dept = sc.nextLine();
            
            String query = "INSERT INTO students VALUES(" + roll + ", '" + name + "', '" + dept + "')";
            stmt.executeUpdate(query);
            
            System.out.println("✓ Student added successfully!");
            
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    // Display All Students
    static void displayStudents() {
        try {
            ResultSet rs = stmt.executeQuery("SELECT * FROM students ORDER BY roll_no");
            
            System.out.println("\n========== STUDENT RECORDS ==========");
            System.out.printf("%-10s %-20s %-15s\n", "Roll No", "Name", "Department");
            System.out.println("---------------------------------------------");
            
            int count = 0;
            while (rs.next()) {
                System.out.printf("%-10d %-20s %-15s\n",
                    rs.getInt("roll_no"),
                    rs.getString("name"),
                    rs.getString("dept"));
                count++;
            }
            
            System.out.println("---------------------------------------------");
            System.out.println("Total Records: " + count);
            
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    // Update Student
    static void updateStudent() {
        try {
            System.out.print("Enter Roll No to update: ");
            int roll = sc.nextInt();
            sc.nextLine();
            
            System.out.print("Enter New Name: ");
            String name = sc.nextLine();
            
            System.out.print("Enter New Department: ");
            String dept = sc.nextLine();
            
            String query = "UPDATE students SET name='" + name + "', dept='" + dept 
                + "' WHERE roll_no=" + roll;
            
            int rows = stmt.executeUpdate(query);
            
            if (rows > 0) {
                System.out.println("✓ Student updated successfully!");
            } else {
                System.out.println("✗ Student not found!");
            }
            
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    // Delete Student
    static void deleteStudent() {
        try {
            System.out.print("Enter Roll No to delete: ");
            int roll = sc.nextInt();
            
            String query = "DELETE FROM students WHERE roll_no=" + roll;
            int rows = stmt.executeUpdate(query);
            
            if (rows > 0) {
                System.out.println("✓ Student deleted successfully!");
            } else {
                System.out.println("✗ Student not found!");
            }
            
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    // Search Student
    static void searchStudent() {
        try {
            System.out.print("Enter Roll No to search: ");
            int roll = sc.nextInt();
            
            ResultSet rs = stmt.executeQuery("SELECT * FROM students WHERE roll_no=" + roll);
            
            if (rs.next()) {
                System.out.println("\n========== STUDENT DETAILS ==========");
                System.out.println("Roll No    : " + rs.getInt("roll_no"));
                System.out.println("Name       : " + rs.getString("name"));
                System.out.println("Department : " + rs.getString("dept"));
            } else {
                System.out.println("✗ Student not found!");
            }
            
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

### **Python + MySQL Database Connectivity**

```python
# ============================================
# DATABASE CONNECTIVITY USING PYTHON
# ============================================

import mysql.connector
from mysql.connector import Error

class StudentManagement:
    def __init__(self):
        try:
            # Create connection
            self.connection = mysql.connector.connect(
                host='localhost',
                database='college_db',
                user='root',
                password='your_password'
            )
            
            if self.connection.is_connected():
                print("✓ Database Connected Successfully!")
                self.cursor = self.connection.cursor()
                
        except Error as e:
            print(f"Error: {e}")
    
    def add_student(self):
        try:
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            
            query = "INSERT INTO students VALUES (%s, %s, %s)"
            values = (roll, name, dept)
            
            self.cursor.execute(query, values)
            self.connection.commit()
            
            print("✓ Student added successfully!")
            
        except Error as e:
            print(f"Error: {e}")
    
    def display_students(self):
        try:
            self.cursor.execute("SELECT * FROM students ORDER BY roll_no")
            records = self.cursor.fetchall()
            
            print("\n========== STUDENT RECORDS ==========")
            print(f"{'Roll No':<10} {'Name':<20} {'Department':<15}")
            print("-" * 45)
            
            for row in records:
                print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15}")
            
            print("-" * 45)
            print(f"Total Records: {len(records)}")
            
        except Error as e:
            print(f"Error: {e}")
    
    def update_student(self):
        try:
            roll = int(input("Enter Roll No to update: "))
            name = input("Enter New Name: ")
            dept = input("Enter New Department: ")
            
            query = "UPDATE students SET name=%s, dept=%s WHERE roll_no=%s"
            values = (name, dept, roll)
            
            self.cursor.execute(query, values)
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print("✓ Student updated successfully!")
            else:
                print("✗ Student not found!")
                
        except Error as e:
            print(f"Error: {e}")
    
    def delete_student(self):
        try:
            roll = int(input("Enter Roll No to delete: "))
            
            query = "DELETE FROM students WHERE roll_no=%s"
            self.cursor.execute(query, (roll,))
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print("✓ Student deleted successfully!")
            else:
                print("✗ Student not found!")
                
        except Error as e:
            print(f"Error: {e}")
    
    def search_student(self):
        try:
            roll = int(input("Enter Roll No to search: "))
            
            query = "SELECT * FROM students WHERE roll_no=%s"
            self.cursor.execute(query, (roll,))
            record = self.cursor.fetchone()
            
            if record:
                print("\n========== STUDENT DETAILS ==========")
                print(f"Roll No    : {record[0]}")
                print(f"Name       : {record[1]}")
                print(f"Department : {record[2]}")
            else:
                print("✗ Student not found!")
                
        except Error as e:
            print(f"Error: {e}")
    
    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("✓ Connection closed successfully!")

# Main Program
def main():
    db = StudentManagement()
    
    while True:
        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.display_students()
        elif choice == '3':
            db.update_student()
        elif choice == '4':
            db.delete_student()
        elif choice == '5':
            db.search_student()
        elif choice == '6':
            db.close_connection()
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
```

---

## 📝 **Database Setup SQL**

```sql
-- ============================================
-- DATABASE SETUP FOR ALL EXPERIMENTS
-- ============================================

-- For Experiment 6
CREATE DATABASE college_db;
USE college_db;

CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    dept VARCHAR(50) NOT NULL
);

-- Insert Sample Data
INSERT INTO students VALUES (1, 'Amit Kumar', 'Computer');
INSERT INTO students VALUES (2, 'Priya Singh', 'IT');
INSERT INTO students VALUES (3, 'Rahul Patil', 'E&TC');
INSERT INTO students VALUES (4, 'Sneha Desai', 'Computer');
INSERT INTO students VALUES (5, 'Vikram Sharma', 'Mechanical');

-- Verify
SELECT * FROM students;
```

---

## 🎯 **How to Run the Code**

### **For Java:**
1. **Install MySQL JDBC Driver:**
   - Download `mysql-connector-java-8.0.xx.jar`
   - Add to classpath

2. **Compile and Run:**
```bash
javac -cp .:mysql-connector-java-8.0.xx.jar StudentManagement.java
java -cp .:mysql-connector-java-8.0.xx.jar StudentManagement
```

### **For Python:**
1. **Install MySQL Connector:**
```bash
pip install mysql-connector-python
```

2. **Run:**
```bash
python student_management.py
```

### **For SQL Scripts:**
1. **Login to MySQL:**
```bash
mysql -u root -p
```

2. **Run Scripts:**
```sql
source experiment1.sql;
```

---

## ✅ **Pre-Practical Checklist**

- [ ] MySQL/Oracle installed and running
- [ ] MongoDB installed (for Experiment 3)
- [ ] Know your database username/password
- [ ] All tables created with sample data
- [ ] Java JDK installed (for Experiment 6)
- [ ] JDBC driver downloaded
- [ ] Practice each experiment at least once
- [ ] Understand the logic, not just syntax
- [ ] Know how to handle common errors

---

## 🚀 **Quick Tips for Practical Exam**

1. **Test your database connection first**
2. **Insert sample data before running queries**
3. **Use meaningful variable names**
4. **Add comments to explain logic**
5. **Handle exceptions properly**
6. **Test with different inputs**
7. **Keep your code clean and formatted**
8. **Save your work frequently**

---

**Good luck with your mock practical! 🎓**

If you need any specific code explained or have questions about any experiment, feel free to ask!