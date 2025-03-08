def read_from_file():
    with open("example.txt", "r") as file:
        # content = file.read()
        # print(content)

        # lines = [line.rstrip() for line in file]
        # print(lines)

        lines = file.readlines()
        print(lines)


def write_to_file():
    with open("example_data.txt", "w") as file:
        number = 123
        file.write(f"{number}\n")
        number += 1
        file.write(f"{number}\n")


if __name__ == '__main__':
    # read_from_file()
    write_to_file()