def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


def add(*args):
    result = 0
    for num in args:
        result += num
    return result


square = lambda x: x ** 2

if __name__ == '__main__':
    # print(greet("Alice"))  # Uses the default greeting
    # print(greet("Bob", "Hi"))  # Uses a custom greeting

    # print(add(1, 2, 3, 4, 5))  # Any number of arguments can be passed

    print(square(4))
