#Class Method and Instance Method
class Sample:
    count = 0

    def __init__(self):
        Sample.count += 1

    def instance_method(self):
        print("This is an instance:")

    @classmethod
    def class_method(cls):
        print(f"Total objects created: {cls.count}")

obj1 = Sample()
obj2 = Sample()
obj1.instance_method()
Sample.class_method()
