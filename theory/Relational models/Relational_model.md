# Relational Model

## Architecture

Proposed in 70s by Edgar Frank Codd at IBM, the relational model is a database model based on the mathematical concept of a relation. A relation is a table with columns and rows. The columns have a name and a type, and the rows are the records of the table.

Its widely used in the industry because of its simplicity and flexibility. Also it is a `madure` model, with a lot of tools and resources available.

Very usefull to **big data** and **data science**.

### For what is used?

- **Large transactional volume**: It is used in systems that need to process a large number of transactions quickly and efficiently. For example, a bank system that needs to process millions of transactions every day. This requires a `CRUD` operation.

- **It is quick and efficient**: It is designed to process transactions quickly and accurately. It is optimized for processing a large number of transactions at the same time.

- **Data integrity**: It is designed to ensure that the data is accurate and consistent. It is designed to ensure that the data is accurate and consistent.

- **Avoid data redundancy**: It is designed to avoid data redundancy. It is designed to avoid data redundancy.

- **Keeps concurrent data**: It is designed to keep the data up-to-date. It is designed to keep the data up-to-date.

### Weaknesses

- **Analyse data**: It is not designed to analyze data.

- **Historical data**: It is not designed to keep historical data.

- **Data Scalability**: It is not designed to handle a large amount of data.

- **data redundancy**: It is not designed to keep a archive of data.

---

This type of architeture is designed to `Transaction Processing` and `Data Integrity`.

## ACID Properties

The ACID properties are a set of properties that guarantee that database transactions are processed reliably. The ACID properties are:

- **Atomicity**

- **Consistency**

- **Isolation**

- **Durability**

### Atomicity

If one of the operations fails, the entire transaction is rolled back. This ensures that the database is always in a consistent state.

This structure follows the commit and rollback operations. If the transaction is successful, the changes are committed to the database. If the transaction fails, the changes are rolled back.

### Consistency

Consistency rule is that the database must always be in a consistent state. For example if a row that contains a foreign key is deleted, the database will not allow the deletion of the row that contains the primary key. 

This can be changed by the use of `CASCADE` or `SET NULL` in the foreign key.

### Isolation

Isolation rule is that the database must be isolated from other transactions. This means that the database must be able to handle multiple transactions at the same time without interfering with each other.

### Durability

Durability rule is that the database must be able to recover from a failure. This means that the database must be able to recover from a failure and return to a consistent state.

If a transaction is done, the changes are permanent and will not be lost.