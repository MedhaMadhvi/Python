# Write a Python program to create a class named Student with attributes name, age and grade. Implement a method to display the student’s information in a formatted string.
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_information(self):
        print("Name: ",self.name)
        print("Age: ", self.age)
        print("Grade: ", self.grade)

name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
grade = input("Enter the student's grade: ")

student = Student(name, age, grade)

print("Student Information:")
student.display_information()