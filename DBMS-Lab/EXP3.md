# 🧪 Experiment No. 3 — MongoDB CRUD Operations on Library Collection

## 🎯 Aim

To perform **MongoDB Queries** using **CRUD operations (Create, Read, Update, Delete)** and logical operators.

---

## 📘 Objectives

* Understand and execute **basic CRUD operations** in MongoDB.
* Learn to use **logical operators** like `$and` and `$or`.
* Perform database operations using **MongoDB shell commands**.

---

## 🧠 Theory (Viva Notes)

### 🔹 What is MongoDB?

MongoDB is a **NoSQL**, **document-oriented** database that stores data in **BSON/JSON-like documents** instead of tables.
It provides **flexibility**, **scalability**, and **high performance** for modern applications.

---

### 🔹 CRUD Operations in MongoDB

| Operation  | Command                               | Description                          |
| ---------- | ------------------------------------- | ------------------------------------ |
| **Create** | `insertOne()`, `insertMany()`         | Adds new documents to a collection.  |
| **Read**   | `find()`, `findOne()`                 | Retrieves data from the database.    |
| **Update** | `updateOne()`, `updateMany()`, `$set` | Modifies existing documents.         |
| **Delete** | `deleteOne()`, `deleteMany()`         | Removes documents from a collection. |

---

### 🔹 Logical Operators

| Operator                     | Use                                                      |
| ---------------------------- | -------------------------------------------------------- |
| `$or`                        | Returns documents that match **at least one** condition. |
| `$and`                       | Returns documents that match **all** conditions.         |
| `$gt`, `$lt`, `$gte`, `$lte` | Compare numerical values.                                |

---

## 💻 Code (MongoDB Shell Script)

```js
// ---------------- CREATE OPERATIONS ----------------
// Create a new collection named 'library'
db.createCollection("library")

// Insert one document
db.library.insertOne({ "bid": 1, "name": "C++" })

// Insert more documents
db.library.insertOne({ "bid": 2, "name": "Python" })
db.library.insertOne({ "bid": 3, "name": "Java" })

// Insert multiple documents at once
db.library.insertMany([
 { "bid": 4, "name": "MongoDB" },
 { "bid": 5, "name": "Data Structures" }
])

// ---------------- READ OPERATIONS ----------------
// Display all documents from library collection
db.library.find().pretty()

// Find a specific book by name
db.library.find({ name: "Python" }).pretty()

// Find all books where bid > 2
db.library.find({ bid: { $gt: 2 } }).pretty()

// Display books in ascending order by name
db.library.find().sort({ name: 1 }).pretty()

// Display only the first 3 documents
db.library.find().limit(3).pretty()

// ---------------- UPDATE OPERATIONS ----------------
// Update one book's name from 'C++' to 'Advanced C++ Programming'
db.library.updateOne(
 { name: "C++" },
 { $set: { name: "Advanced C++ Programming" } }
)

// Update multiple documents where bid < 4 and add a new field 'category'
db.library.updateMany(
 { bid: { $lt: 4 } },
 { $set: { category: "Programming" } }
)

// Using save() method to replace or insert document
db.library.save({
 _id: ObjectId("PUT_EXISTING_OBJECT_ID_HERE"),
 bid: 6,
 name: "Database Systems"
})

// ---------------- DELETE OPERATIONS ----------------
// Delete one document (book named 'Java')
db.library.deleteOne({ name: "Java" })

// Delete multiple documents where bid >= 5
db.library.deleteMany({ bid: { $gte: 5 } })

// Delete all documents (use with caution!)
db.library.deleteMany({})

// ---------------- LOGICAL OPERATORS ----------------
// OR operator: find books named 'Python' or 'Java'
db.library.find({
 $or: [{ name: "Python" }, { name: "Java" }]
}).pretty()

// AND condition: find books with bid > 1 AND name = 'Python'
db.library.find({
 bid: { $gt: 1 },
 name: "Python"
}).pretty()
```

---

## 🧾 Output

✅ All CRUD operations executed successfully on the **`library`** collection.
The documents were **inserted, retrieved, updated, and deleted** as expected.

---

## 🏁 Conclusion

Thus, we have successfully **performed and verified MongoDB CRUD operations**
(**Create**, **Read**, **Update**, **Delete**) using MongoDB shell commands and logical operators.