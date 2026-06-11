CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100),
 age INT,
 course VARCHAR(100)
 );

INSERT INTO students (name,age,course)
 VALUES("Riya Sharma", 18, "Data Science");
 
INSERT INTO students (name,age,course)
VALUES ("Aryan Goyal", 20, "Computer Science");
 
INSERT INTO students (name,age,course)
VALUES("Myra Singh", 19, "Electronics");

SELECT*FROM students;

DELETE FROM students WHERE id=1;
UPDATE students SET id=1 WHERE name= "Riya Sharma";
SET SQL_SAFE_UPDATES = 0;

DELETE FROM students WHERE id=4;
UPDATE students SET id=2 WHERE name= "Aryan Goyal";
UPDATE students SET id=3 WHERE name= "Myra Singh";


