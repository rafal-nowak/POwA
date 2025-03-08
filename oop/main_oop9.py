class Parent1:
    def method1(self):
        print("Method 1 from Parent1")


class Parent2:
    def method2(self):
        print("Method 2 from Parent2")


# Child class inherits from both Parent1 and Parent2
class Child(Parent1, Parent2):
    def child_method(self):
        print("Child's own method")


if __name__ == '__main__':
    # Create an instance of the Child class
    child = Child()

    # Call methods from both parent classes
    child.method1()  # Output: Method 1 from Parent1
    child.method2()  # Output: Method 2 from Parent2
    child.child_method()  # Output: Child's own method
