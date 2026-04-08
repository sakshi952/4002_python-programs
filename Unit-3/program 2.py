#Student Class with Add and Display Methods
class Student:
    def __init__(self):
        self.roll = None
        self.name = None
        self.age = None
        self.gender = None

    def add_student(self):
        self.roll = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")

    def display_student(self):
        print(f"Roll No: {self.roll}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

s = Student()
s.add_student()
s.display_student()
