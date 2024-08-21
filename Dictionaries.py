# 1. Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eva"
}

# 1.1 Adding the values in dictionary
def add_student(student_id, student_name):
    students[student_id] = student_name
    print(f"Added student: {student_id} - {student_name}")

add_student(106, "Frank")

# 1.2 Updating the values in dictionary
def update_student(student_id, new_name):
    if student_id in students:
        students[student_id] = new_name
        print(f"Updated student: {student_id} - {new_name}")
    else:
        print(f"Student ID {student_id} not found.")

update_student(103, "Chuck")

# 1.3 Accessing the value in dictionary
def get_student_name(student_id):
    return students.get(student_id, "Student not found")

print(f"Student 101's name: {get_student_name(101)}")

# 1.4 Create a nested dictionary
nested_students = {
    "class1": {
        201: "Tom",
        202: "Jerry"
    },
    "class2": {
        301: "Spike",
        302: "Tyke"
    }
}

# 1.5 Access the values of nested dictionary
def get_nested_student_name(class_id, student_id):
    class_dict = nested_students.get(class_id, {})
    return class_dict.get(student_id, "Student not found in this class")

print(f"Student 201's name in class1: {get_nested_student_name('class1', 201)}")
print(f"Student 302's name in class2: {get_nested_student_name('class2', 302)}")

# 1.6 Print the keys present in a particular dictionary
def print_keys(dictionary):
    print("Keys in dictionary:")
    for key in dictionary:
        print(key)

print("\nKeys in students dictionary:")
print_keys(students)

print("\nKeys in nested_students dictionary:")
for class_id, class_dict in nested_students.items():
    print(f"Keys in {class_id}:")
    print_keys(class_dict)

# 1.7 Delete a value from a dictionary
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Deleted student ID: {student_id}")
    else:
        print(f"Student ID {student_id} not found.")

delete_student(105)

# Print updated dictionaries
print("\nUpdated students dictionary:")
print(students)

print("\nUpdated nested_students dictionary:")
print(nested_students)
