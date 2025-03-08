class Circle:
    # Class attribute
    pi = 3.14159265359

    def __init__(self, radius):
        # Instance attribute
        self.radius = radius

    # Instance method
    def area(self):
        return self.pi * (self.radius ** 2)

    # Class method
    @classmethod
    def set_pi(cls, value):
        cls.pi = value


if __name__ == '__main__':
    circle1 = Circle(5)
    print("Circle 1 Area:", circle1.area())

    Circle.set_pi(3.14)  # Modify the class attribute
    circle2 = Circle(3)
    print("Circle 2 Area:", circle2.area())