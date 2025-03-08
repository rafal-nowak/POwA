def add(x, y):
    return x + y


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Circle:
    pi = 3.14159265359

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def set_pi(cls, value):
        cls.pi = value


if __name__ == '__main__':
    result = add(3, 4)

    person1 = Person("Alice", 25)
    message = person1.greet()

    Circle.set_pi(3.14)  # Modify the class attribute pi for all instances
