# 🧪 Experiment No. 5 — PL/SQL Cursors (All Types)

## 🎯 Aim

To write and execute PL/SQL blocks using all types of cursors — **Implicit, Explicit, Cursor FOR Loop, and Parameterized Cursor** — for merging records from a new table `N_Roll_Call` into an existing table `O_Roll_Call`, avoiding duplicate entries.

---

## 📘 Objectives

* To understand different types of **cursors** in PL/SQL.
* To implement a **parameterized cursor** for merging data between tables.
* To use **cursor operations** for controlled data traversal and manipulation.

---

## 🧠 Theory (Viva Notes)

### 🔹 What is a Cursor?

A **cursor** in PL/SQL is a **pointer to the result set** of a query. It allows row-by-row processing of query results.

### 🔹 Types of Cursors

| Type                     | Description                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Implicit Cursor**      | Automatically created by Oracle for DML statements like `INSERT`, `UPDATE`, `DELETE`, `SELECT INTO`. |
| **Explicit Cursor**      | Declared explicitly by the programmer to fetch query results manually.                               |
| **Cursor FOR Loop**      | Simplifies cursor usage by handling open, fetch, and close automatically.                            |
| **Parameterized Cursor** | Accepts parameters for dynamic query execution, allowing filtering at runtime.                       |

### 🔹 Why Use Cursors?

Cursors are used when multiple records must be processed one by one, especially during **data migration, validation, or merging** between tables.

---

## 💻 Code Implementation

### 🗂️ Step 1: Create Tables

```sql
CREATE TABLE o_rollcall (
  roll_no NUMBER,
  name VARCHAR2(25),
  div VARCHAR2(5)
);

CREATE TABLE n_rollcall (
  roll_no NUMBER,
  name VARCHAR2(25),
  div VARCHAR2(5)
);
```

---

### 🧾 Step 2: Insert Sample Data into `O_Roll_Call`

```sql
INSERT INTO o_rollcall VALUES (11, 'ABHISHEK', 'A');
INSERT INTO o_rollcall VALUES (12, 'SAKSHI', 'A');
INSERT INTO o_rollcall VALUES (13, 'SANKET', 'B');
INSERT INTO o_rollcall VALUES (14, 'MAYUR', 'A');
INSERT INTO o_rollcall VALUES (15, 'ROHAN', 'B');
INSERT INTO o_rollcall VALUES (16, 'SANJU', 'B');
```

---

### ⚙️ Step 3: PL/SQL Block using Parameterized Cursor

```sql
SET SERVEROUTPUT ON;
SET VERIFY OFF;

CREATE OR REPLACE PROCEDURE cursor_imp AS
  c_r NUMBER;
  c_n VARCHAR2(25);
  c_d VARCHAR2(5);

  -- Parameterized cursor to find duplicate records in o_rollcall
  CURSOR c1 (roll NUMBER, n VARCHAR2, d VARCHAR2) IS
    SELECT roll_no, COUNT(roll_no),
           name, COUNT(name),
           div, COUNT(div)
    FROM o_rollcall
    GROUP BY roll_no, name, div
    HAVING (COUNT(roll_no) > 1)
       AND (COUNT(name) > 1)
       AND (COUNT(div) > 1);

  temp c1%ROWTYPE;

BEGIN
  -- Clear and refill n_rollcall table
  DELETE FROM n_rollcall;
  INSERT INTO n_rollcall SELECT * FROM o_rollcall;

  -- Open and process cursor
  OPEN c1(c_r, c_n, c_d);
  LOOP
    FETCH c1 INTO temp;
    EXIT WHEN c1%NOTFOUND;

    -- If duplicate found, remove and reinsert (merging logic)
    DELETE FROM n_rollcall
     WHERE roll_no = temp.roll_no
       AND name = temp.name
       AND div = temp.div;

    INSERT INTO n_rollcall VALUES (temp.roll_no, temp.name, temp.div);
    DBMS_OUTPUT.PUT_LINE(temp.roll_no || ' ' || temp.name || ' ' || temp.div);
  END LOOP;

  CLOSE c1;
END;
/

-- Execute the procedure
BEGIN
  cursor_imp;
END;
/
```

---

## 🧾 Step 4: View Merged Data

```sql
SELECT * FROM n_rollcall;
```

### ✅ Output

| ROLL_NO | NAME     | DIV |
| ------- | -------- | --- |
| 11      | ABHISHEK | A   |
| 12      | SAKSHI   | A   |
| 13      | SANKET   | B   |
| 14      | MAYUR    | A   |
| 15      | ROHAN    | B   |
| 16      | SANJU    | B   |

---

## 🧩 Explanation (Quick Viva Recap)

* `CURSOR c1` is **parameterized**, allowing flexibility to filter data dynamically.
* The **loop** fetches each record and merges it into `n_rollcall`.
* The procedure avoids duplicate records by deleting and reinserting unique entries.
* `DBMS_OUTPUT.PUT_LINE` displays merged records for verification.
* The process demonstrates how to use **parameterized cursors** to manage data row by row.

---

## 🏁 Conclusion

Thus, we have successfully implemented and executed a **PL/SQL procedure using a parameterized cursor** to merge records from one table to another while skipping duplicate entries.
This experiment helped in understanding all types of cursors and their use in real-time data operations.