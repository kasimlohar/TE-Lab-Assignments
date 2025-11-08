# 🧪 Experiment No. 6 — Database Connectivity using Java and MySQL

## 🎯 Aim

To write a Java program to establish connectivity between **Java (front-end)** and **MySQL (back-end)** to perform **database navigation operations** such as **Add, Display, Update, and Delete**.

---

## 📘 Objectives

* To understand the concept of **JDBC (Java Database Connectivity)**.
* To connect Java applications to a MySQL database.
* To execute **SQL queries** through Java.
* To perform database navigation operations interactively using the console.

---

## 🧠 Theory (Viva Notes)

### 🔹 What is JDBC?

JDBC (Java Database Connectivity) is an **API** that allows Java programs to **connect to databases**, execute SQL statements, and process results.

### 🔹 JDBC Architecture

1. **JDBC Driver** – Provides the connection interface (e.g., MySQL Connector/J).
2. **DriverManager** – Manages database drivers and connections.
3. **Connection** – Establishes a link between Java and the database.
4. **Statement / PreparedStatement** – Used to send SQL queries.
5. **ResultSet** – Holds the results retrieved from the database.

### 🔹 Steps for JDBC Connection

1. **Load the Driver:** `Class.forName("com.mysql.cj.jdbc.Driver");`
2. **Establish Connection:** `DriverManager.getConnection(url, user, password);`
3. **Create Statement:** `Statement sm = c.createStatement();`
4. **Execute SQL Queries:** `sm.executeUpdate()` or `sm.executeQuery()`
5. **Process ResultSet:** Use `while(rs.next())` loop.
6. **Close Connection:** `c.close();`

---

## 💻 Java Program: Database Connectivity (CRUD Operations)

```java
package matoshri;
import java.sql.*;
import java.util.Scanner;

public class DeptDB {
    public static void main(String[] args) {
        try {
            Scanner input = new Scanner(System.in);

            // Step 1: Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 2: Establish Connection
            Connection c = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/practical", 
                "student", 
                "Student@123"
            );

            Statement sm = c.createStatement();
            System.out.println("Database Connected...");

            int ch;

            // Step 3: Menu-driven database operations
            do {
                System.out.println("Enter Choice: \n 1.Insert \n 2.Select \n 3.Update \n 4.Delete \n 5.Exit ");
                ch = input.nextInt();

                switch (ch) {

                    // INSERT Operation
                    case 1:
                        String sql = "INSERT INTO Student VALUES(8,1010,'Pooja','Deore',18,'Nashik');";
                        sm.executeUpdate(sql);
                        System.out.println("Record is Inserted...");
                        break;

                    // SELECT Operation
                    case 2:
                        sql = "SELECT first_name, last_name, age, city FROM Student";
                        ResultSet rs = sm.executeQuery(sql);
                        while (rs.next()) {
                            String fname = rs.getString("first_name");
                            String lname = rs.getString("last_name");
                            int age = rs.getInt("age");
                            String city = rs.getString("city");

                            System.out.println("First Name: " + fname);
                            System.out.println("Last Name: " + lname);
                            System.out.println("Age: " + age);
                            System.out.println("City: " + city);
                        }
                        break;

                    // UPDATE Operation
                    case 3:
                        sql = "UPDATE Student SET first_name='Manoj' WHERE id = 5;";
                        sm.executeUpdate(sql);
                        System.out.println("Record is Updated...");
                        break;

                    // DELETE Operation
                    case 4:
                        sql = "DELETE FROM Student WHERE id = 8;";
                        sm.executeUpdate(sql);
                        System.out.println("Record is Deleted...");
                        break;
                }
            } while (ch < 5); // Exit condition

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## 🧾 Sample Output

```
Database Connected...
Enter Choice
 1.Insert
 2.Select
 3.Update
 4.Delete
 5.Exit
1
Record is Inserted...

Enter Choice
2
First Name: Shital
Last Name: Gayke
Age: 18
City: Sinnar
First Name: Sakshi
Last Name: More
Age: 19
City: Nashik
First Name: Ajay
Last Name: Mendade
Age: 18
City: Satpur
First Name: Manoj
Last Name: More
Age: 19
City: Wani
First Name: Alok
Last Name: Pandit
Age: 18
City: Nashik
First Name: Sanju
Last Name: Banka
Age: 18
City: Bhagur
First Name: Pooja
Last Name: Deore
Age: 18
City: Nashik

Enter Choice
3
Record is Updated...

Enter Choice
4
Record is Deleted...

Enter Choice
5
```

---

## 🧩 Explanation

* The program uses **Java JDBC** to connect with the **MySQL** database.
* A **menu-driven interface** allows users to:

  * **Insert** new records
  * **Select** (display) all student records
  * **Update** existing data
  * **Delete** specific records
* Connection parameters include:

  * Database: `practical`
  * User: `student`
  * Password: `Student@123`
* The driver `com.mysql.cj.jdbc.Driver` is loaded for MySQL 8+.
* SQL queries are executed using the `Statement` object.
* Output is displayed using `ResultSet`.

---

## 🏁 Conclusion

Thus, a Java program was successfully developed to connect with a **MySQL database** using **JDBC**.
The program performed all major **CRUD (Create, Read, Update, Delete)** operations and demonstrated effective **database navigation** through a front-end (Java console).
