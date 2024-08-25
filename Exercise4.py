# Class definition for Student
from Lib.Exercise1 import student_id


class Student:
    def __init__(self, name, age, student_id, batch_number):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.batch_number = batch_number

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Batch Number: {self.batch_number}")

# Creating an instance of the Student class by taking input
name = input("Enter your name:")
age = int(input("Enter your age:"))
student_id = input("Enter your studnet ID:")
batch_number = int(input("Enter your batch number:"))

student = Student(name, age, student_id, batch_number)

# Displaying student information
student.display_student_info()
