import csv


if __name__ == '__main__':
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

    # with open("example.txt", "w") as file:
    #     file.write("This is a line of text.")

    # with open("data.csv", "w") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["no", "temperature"])
    #     writer.writerow([1, 26.1])
    #     writer.writerow([2, 26.3])
    #     writer.writerow([3, 26.7])


    # with open("data.csv", "r") as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         print(row)