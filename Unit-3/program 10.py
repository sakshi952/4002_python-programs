#operator overloading + and -
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __str__(self):
        return str(self.value)

a = Number(10)
b = Number(5)
print("Addition:", a + b)
print("Subtraction:", a - b)
