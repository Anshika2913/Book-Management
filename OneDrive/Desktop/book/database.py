CREATE DATABASE bookshop;

USE bookshop;

CREATE TABLE books (
    b_id INT PRIMARY KEY,
    book_name VARCHAR(255) NOT NULL,
    author_name VARCHAR(255),
    year VARCHAR(4),
    price DECIMAL(10, 2),
    type VARCHAR(50),
    quantity INT
);

``` ```sql
CREATE TABLE customers (
    cno INT PRIMARY KEY,
    cname VARCHAR(255) NOT NULL,
    bookpurchase VARCHAR(255),
    price DECIMAL(10, 2),
    dateofpurchase DATE,
    authorname VARCHAR(255),
    contactno VARCHAR(15),
    address TEXT
);
