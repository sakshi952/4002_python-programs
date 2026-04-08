
#inheritance -> student course
class Student:
    def __init__(self, roll, name, gender, age):
        self.roll = roll
        self.name = name
        self.gender = gender
        self.age = age

class Course(Student):
    def __init__(self, roll, name, gender, age, course_name, duration, fee):
        super().__init__(roll, name, gender, age)
        self.course_name = course_name
        self.duration = duration
        self.fee = fee

    def display(self):
        print(f"{self.roll} | {self.name} | {self.gender} | {self.age} | {self.course_name} | {self.duration} | ₹{self.fee}")

c = Course("101", "Anita", "Female", 21, "MCA", "2 Years", 120000)
c.display()
