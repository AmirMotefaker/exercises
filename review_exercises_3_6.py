# Code by @Amir Motefaker
# Review Exercises Chapter 3 #6

# 6. In what cases should different types of data be used?
# - Give an example where the appropriate type of data storage is a list.
# - Give another example where a dictionary data type is suitable for storing data.
# - Give an example that requires you to store multiple types of data.
# - Design a dictionary that stores several types of data, including internal data
#   Also have different data in them.

# - Give an example where the appropriate type of data storage is a list.
marks = [20, 11, 10, 18]

# - Give another example where a dictionary data type is suitable for storing data.
my_student = {
    "name": "Ana",
    "age": 20,
    "lastname": "Johnson",
    "marks": [
        {
            "title": "math",
            "mark": 20
        },
        {
            "title": "chem",
            "mark": 12
        }
    ]
}

# print(my_student['age'])
print(my_student["marks"][1]["mark"])
