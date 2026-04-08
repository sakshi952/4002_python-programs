#interface simulation
class Printable:
    def print_data(self):
        raise NotImplementedError

class Student(Printable):
    def __init__(self, name):
        self.name = name

    def print_data(self):
        print("Student Name:", self.name)

s = Student("Rahul")
s.print_data()
