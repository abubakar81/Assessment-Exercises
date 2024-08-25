# Initial score based on the sum of the last four digits of the student ID
initial_score = sum([int(digit) for digit in "0043"])

# Dictionary to store student names and scores
students = {}

# Function to add a student
def add_student(name):
    students[name] = initial_score
    print(f"Added {name} with initial score {initial_score}.")

# Function to remove a student
def remove_student(name):
    if name in students:
        del students[name]
        print(f"Removed {name} from the list.")
    else:
        print(f"{name} not found.")

# Function to display all students
def display_students():
    if students:
        print("Student Name - Score")
        for name, score in students.items():
            print(f"{name} - {score}")
    else:
        print("No students to display.")


# Sample operations
new_student = input("Add a student:")
add_student(new_student)
new_student = input("Add a student:")
add_student(new_student)
display_students()
student_to_remove = input("Remove a student:")
remove_student(student_to_remove)
display_students()
