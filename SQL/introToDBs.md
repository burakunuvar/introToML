### Introduction 

- SQL is a language. Hence, the last word of SQL being language. SQL is used all over the place beyond the databases but is most popular for its interaction with databases.

**Advantages**
  - SQL is easy to understand.
  - Traditional databases allow us to access data directly.
  - Traditional databases allow us to audit and replicate our data.
  - SQL is a great tool for analyzing multiple tables at once.
  - SQL allows you to analyze more complex questions than dashboard tools like Google Analytics.


**Why Businesses Like Databases**

- Data integrity is ensured - only the data you want entered is entered, and only certain users are able to enter data into the database.

- Data can be accessed quickly - SQL allows you to obtain results very quickly from the data stored in a database. Code can be optimized to quickly pull results.

- Data is easily shared - multiple individuals can access data stored in a database, and the data is the same for all users allowing for consistent results for anyone with access to your database.

**A few key points about data stored in SQL databases:**

- Data in databases is stored in tables that can be thought of just like Excel spreadsheets.
For the most part, you can think of a database as a bunch of Excel spreadsheets. Each spreadsheet has rows and columns. Where each row holds data on a transaction, a person, a company, etc., while each column holds data pertaining to a particular aspect of one of the rows you care about like a name, location, a unique id, etc.

- All the data in the same column must match in terms of data type.
An entire column is considered quantitative, discrete, or as some sort of string. This means if you have one row with a string in a particular column, the entire column might change to a text data type. This can be very bad if you want to do math with this column!

- Consistent column types are one of the main reasons working with databases is fast.
Often databases hold a LOT of data. So, knowing that the columns are all of the same type of data means that obtaining data from a database can still be fast.

**Types of Databases**

- NoSQL stands for not only SQL. Databases using NoSQL allow for you to write code that interacts with the data a bit differently. These NoSQL environments tend to be particularly popular for web based data, but less popular for data that lives in spreadsheets.

- Some of the most popular databases include:
    - MySQL
    - Access
    - Oracle
    - Microsoft SQL Server
    - Postgres
    - also write SQL within other programming frameworks like Python, Scala, and HaDoop

- [The article here](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)) compares three of the most common types of SQL

### SQL Statements

The key to SQL is understanding statements. A few statements include:

 - `CREATE TABLE` is a statement that creates a new table in a database.
 - `DROP TABLE` is a statement that removes a table in a database.
 - `SELECT` allows you to read data and display it. This is called a query.

**Formatting Your Queries**

- SQL queries are **not case-sensitive**, however it is common and best practice to capitalize all SQL commands, like SELECT and FROM, and keep everything else in your query lower case.

Note: The text data stored in SQL tables can be either upper or lower case, and SQL is case-sensitive in regard to this text data

- It is common to use underscores and avoid spaces in column names. It is a bit annoying to work with spaces in SQL. In Postgres if you have spaces in column or table names, you need to refer to these columns/tables with double quotes around them (Ex: `FROM "Table Name"` as opposed to `FROM table_name`). In other environments, you might see this as square brackets instead (Ex: `FROM [Table Name]`)

- SQL queries **ignore spaces**, so you can add as many spaces and blank lines between code as you want, and the queries are the same.

- Depending on your SQL environment, your query **may need a semicolon** at the end to execute. Other environments are more flexible in terms of this being a "requirement." It is considered best practice to put a semicolon at the end of each statement, which also allows you to run multiple queries at once if your environment allows this.

### SQL JOINS

**Database Normalization** 
  - Are the tables storing logical groupings of the data?
  - Can I make changes in a single location, rather than in many tables for the same information?
  - Can I access and manipulate data quickly and efficiently?


**Expert Tip**

You have had a bit of an introduction to these one-to-one and one-to-many relationships when we introduced PKs and FKs. Notice, traditional databases do not allow for many-to-many relationships, as these break the schema down pretty quickly. A very good answer is provided [here (https://stackoverflow.com/questions/7339143/why-no-many-to-many-relationships) .

The types of relationships that exist in a database matter less to analysts, but you do need to understand why you would perform different types of JOINs, and what data you are pulling from the database. These ideas will be expanded upon in the next concepts.

