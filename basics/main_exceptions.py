if __name__ == '__main__':
    # result = 10 / 0

    # try:
    #     result = 10 / 0
    # except ZeroDivisionError:
    #     print("Error: Division by zero")

    # num = int("abc")
    # print(f"num = {num}")

    # try:
    #     num = int("abc")
    #     result = 10 / 0
    # except ValueError:
    #     print("Invalid integer")
    # except Exception as e:
    #     print("An error occurred:", str(e))

    try:
        file = open("example.txt", "r")
        # Perform some operations
    except FileNotFoundError:
        print("File not found")
    finally:
        file.close()  # Ensure the file is closed regardless of exceptions
