# Stage 2 - Student Record System (JSON File)
# Now data is saved to a file so it doesn't get lost

import json
import os

FILE_NAME = "students.json"

# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def get_new_id(students):
    if len(students) == 0:
        return 1
    return students[-1]["id"] + 1

def add_student():
    students = load_students()
    print("\nAdd Student")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student = {
        "id": get_new_id(students),
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    save_students(students)
    print("Student added and saved to file!")

def view_students():
    students = load_students()
    print("\nAll Students")
    if len(students) == 0:
        print("No students found.")
        return
    for s in students:
        print(f"ID: {s['id']} , Name: {s['name']} , Age: {s['age']} , Course: {s['course']}")

def search_student():
    students = load_students()
    print("\nSearch Student")

    name = input("Enter name to search:")
    for s in students:
        if name in s["name"]:
            print(f"ID: {s['id']} ,Name: {s['name']} , Age: {s['age']} , Course: {s['course']}")
            return   

def modify_student():
    students = load_students()
    print("\nModify Student")
    sid = int(input("Enter student ID to update: "))
    for s in students:
     if s["id"] == sid:
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            s["name"] = name
            s["age"] = age
            s["course"] = course
            print("Student modified successfully!")
            return
    print("Student not found.")
                              

def delete_student():
    students = load_students()
    print("\nDelete Student")
    sid = int(input("Enter student ID to delete: "))
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("Student deleted!")
            return
    print("Student not found.")


if not os.path.exists(FILE_NAME):
    sample = [
        {"id": 1, "name": "Riya Sharma", "age": 18,  "course": "Data Science"},
        {"id": 2, "name": "Aryan Goyal",  "age": 20, "course": "Computer Science"},
        {"id": 3, "name": "Myra Singh",   "age": 19, "course": "Electronics"}
    ]
    save_students(sample)
    print("Sample data created in students.json")

print("Welcome to Student Record System - Stage 2 (JSON File)")

while True:
    print("1.View All Students")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Modify Student")
    print("0. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        search_student()
    elif choice == "5":
        modify_student()
    elif choice == "0":
        print("Exiting... data is saved in students.json")
        break
    else:
        print("Invalid choice.")
