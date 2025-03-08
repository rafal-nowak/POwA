def process_student(student):
    print("Student Name:", student["name"])
    print("Student Age:", student["age"])
    print("Student Grade:", student["grade"])


def add_subject(student, subject, score):
    student["subjects"][subject] = score


if __name__ == '__main__':
    # Create a dictionary
    student_info = {"name": "Alice", "age": 20, "grade": "A"}

    # Call the function and pass the dictionary as an argument
    process_student(student_info)

    # Create a dictionary with nested dictionaries
    student_info = {
        "name": "Bob",
        "age": 22,
        "grade": "B",
        "subjects": {"math": 90, "history": 80}
    }

    # Call the function to add a new subject and score
    add_subject(student_info, "chemistry", 85)

    # Print the updated dictionary
    print(student_info)




    student_info = {"name": "Alice", "age": 20, "grade": "A"}

    if "age" in student_info:
        print("The 'age' key exists in the dictionary.")
    else:
        print("The 'age' key does not exist in the dictionary.")



    student_info = {"name": "Alice", "age": 20, "grade": "A"}

    age = student_info.get("age")
    if age is not None:
        print("The 'age' key exists in the dictionary.")
    else:
        print("The 'age' key does not exist in the dictionary.")



    age = student_info.get("age", "N/A")

    student_info = {"name": "Alice", "age": 20, "grade": "A"}

    try:
        age = student_info["age"]
        print("The 'age' key exists in the dictionary.")
    except KeyError:
        print("The 'age' key does not exist in the dictionary.")
