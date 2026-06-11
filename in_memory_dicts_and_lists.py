students = []
new_id = 1

def add_student():
    global new_id
    print("\nAdd Student")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student = {
        "id": new_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    new_id += 1
    print("Student added successfully!")

def view_students():
    print("All Students")
    if len(students) == 0:
        print("No students found.")
        return
    for s in students:
        print(f"ID: {s['id']} , Name: {s['name']} , Age: {s['age']} , Course: {s['course']}")  

students.append({"id": 1, "name": "Riya Sharma","age": 18, "course": "Data Science"})
students.append({"id": 2, "name": "Aryan Goyal", "age": 20, "course": "Computer Science"})
students.append({"id": 3, "name": "Myra Singh",  "age": 19, "course": "Electronics"})
new_id = 4


print("Welcome to Student Record System - Stage 1 (In-Memory Dicts and Lists)")

def delete_student():
    print("Delete Student")
    sid = int(input("Enter student ID to delete:"))
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted!")
    print("Student not found.")        

def search_student():
    print("Search Student")
    name = input("Enter name to search:")
    for s in students:
        if name in s["name"]:
            print(f"ID: {s['id']} ,Name: {s['name']} , Age: {s['age']} , Course: {s['course']}")
            return    

def modify_student():
    print("Modify Student")
    sid = int(input("Enter student ID to modify:"))
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
                              
while True:
    print("\n1. View Students"
          "\n2. Add Student" 
          "\n3. Delete Student"
          "\n4. Search Student"
          "\n5. Modify Student"
          "\n6. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        view_students()
    elif choice == 2:
        add_student()  
    elif choice == 3:
        delete_student()  
    elif choice == 4:
        search_student()    
    elif choice == 5:
        modify_student()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

