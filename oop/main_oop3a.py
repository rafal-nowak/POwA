class Animal:
    def speak(self):
        pass

class Dog():
    def speak(self):
        return "Woof!"

class Cat():
    def speak(self):
        return "Meow!"


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    print(dog.speak())  # Output: "Woof!"
    print(cat.speak())  # Output: "Meow!"