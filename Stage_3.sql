CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100),
 age INT,
 grade FLOAT,
 course VARCHAR(100)
 );

INSERT INTO students (name,age,grade,course)
 VALUES("Riya Sharma", 18,8.5, "Data Science");
 
INSERT INTO students (name,age,grade,course)
VALUES ("Aryan Goyal", 20, 9.1,"Computer Science");
 
INSERT INTO students (name,age,grade,course)
VALUES("Myra Singh", 19, 7.3, "Electronics");

INSERT INTO students(name,age,grade,course)
VALUES("Sneha Verma",18,8.6,"Ai");

INSERT INTO students(name,age,grade,course)
VALUES("Rohan Vohra", 20, 7.8,"Computer Science");

SELECT*FROM students;

DELETE FROM students WHERE id=3;
UPDATE students SET id=5 WHERE name= "Myra Singh";
SET SQL_SAFE_UPDATES = 0;

SELECT course, AVG(grade) AS average_grade
FROM students
GROUP BY course;

SELECT name, grade, course
FROM students
ORDER BY grade DESC
LIMIT 3;

SELECT course, COUNT(*) AS total_students
FROM students
GROUP BY course;


