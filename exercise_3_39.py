# Code by @Amir Motefaker
# Exercises Chapter 3 #39

# 39. Consider the following dictionary:
# student = {
#     "name": "Arash",
#     "mark": 17,
#     "rank": 9,
#     "classes": ['math', 'gym', 'chemistry', 'history'],
#     "parents": {
#         "father": {
#             "name": "Ali",
#             "age": 49
#         },
#         "mother": {
#             "name": "Sara",
#             "age": 46
#         } 
#     }
# }


# At first glance, the above dictionary may be too complicated for you.
# But try to examine it step by step and logically.
# Answer the following questions by considering this dictionary.

# - Try to analyze the reason for writing this dictionary in this way and say why it was made this way. The purpose of this is to give an example of why in one part the list data is used and in another part a string or even a dictionary is used.
# - How to get the list of classes of this student from the above dictionary?
# - According to the dictionary above, if we run the following code, what will be shown to us?
# print(student["parents"])
# - With what code can we access the name of the student's father?
# - According to the above dictionary, what does the following code show us?
# print(student["classes"][3])
# - According to the above dictionary, what does the following code show us?
# print(student["parents"]["father"]["age"])
# - According to the above dictionary, what is the result of the following code?
# print(student["classes"][:2])


student = {
    "name": "Arash",
    "mark": 17,
    "rank": 9,
    "classes": ['math', 'gym', 'chemistry', 'history'],
    "parents": {
        "father": {
            "name": "Ali",
            "age": 49
        },
        "mother": {
            "name": "Sara",
            "age": 46
        } 
    }
}

print(student["classes"])
# Output:
# ['math', 'gym', 'chemistry', 'history']

print(student["parents"])
# Output:
# {'father': {'name': 'Ali', 'age': 49}, 'mother': {'name': 'Sara', 'age': 46}}

print(student["parents"]["father"]["name"])
# Output:
# Ali

print(student["classes"][3])
# Output:
# history

print(student["parents"]["father"]["age"])
# Output:
# 49

print(student["classes"][:2])
# Output:
# ['math', 'gym']
