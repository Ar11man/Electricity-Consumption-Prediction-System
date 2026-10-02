CREATE DATABASE electricity_db;

USE electricity_db;

CREATE TABLE consumption (
    id INT AUTO_INCREMENT PRIMARY KEY,
    consumer_name VARCHAR(100),
    date DATE,
    units_consumed FLOAT
);
