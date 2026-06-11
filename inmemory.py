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


print("Welcome to Student Record System - Stage 1 (In-Memory Dicts and Lists)")

def delete_student():
    print("Delete Student")
    sid = int(input("Enter student ID to delete:"))
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted!")

def search_student():
    print("Search Student")
    name = input("Enter name to search:")
    for s in students:
        if name in s["name"]:
            print(f"ID: {s['id']} ,Name: {s['name']} , Age: {s['age']} , Course: {s['course']}")
            return    

def modify_student():
    print("Modify Student")
    
                              
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