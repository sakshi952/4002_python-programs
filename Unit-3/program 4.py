# Inner Class Usage
class Outer:
    def __init__(self):
        self.inner = self.Inner()

    def show(self):
        print("Outer class method.")
        self.inner.display()

    class Inner:
        def display(self):
            print("Inner class method.")

o = Outer()
o.show()
