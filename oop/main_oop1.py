class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


if __name__ == '__main__':
    person1 = Person("Alice", 25)
    print(person1.greet())