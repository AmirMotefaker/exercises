# Code by @Amir Motefaker
# Exercises Chapter 3 #42

# 42. For each of the following, first say what kind of data is right for it.
# Then say what name you would choose if you wanted to choose the name of the variable properly. 
# For each of them, create a variable and set the value.
# - Example for a student's score (value between 0 and 20)
#      - Sample answer: its gender as int and its variable name as mark_student
# - The age of a person
# - A person's name
# - Save 5 points for a lesson in one variable
# - Save 7 names of people
# - Save the profile of a programmer in a variable that displays the information. Name, surname, age, all languages that worked.
# - Dual storage of a person's name and age in an editable data type
# - The data type is equivalent to the "correct" value for storing whether the air is clear


student_mark = float(input("Enter the student score :"))
age = str(input("Enter the age of the person :"))
name = str(input("Enter the person's name :"))

weather = bool(input("Weather :"))

student = {
    "age": 49,
    "student_mark": [15, 18, 9, 20, 17],
    "name": ["Arash", "Amir", "Ali", "John", "Cris", "Elvin", "Yas"],

    "programmer": {
            "name": "Ali",
            "family": "Motefaker",
            "age": 49,
            "languages": ["Python", "Java", "C"]
            },

     
    "name_age": {
            "name": "Ali",
            "age": 49
            }
}


# Solution 2
age = 25

name = "Amir"

marks = [20, 12, 18, 17, 9]

names = ['amir', 'arad', 'john', 'eli', 'bay']

developer = {
        "first_name" : "Amir",
        "last_name" : "Motefaker",
        "age" : 43,
        "techs" : ['React', 'Django', 'Android'],
}

person_details = ("Ana", 30) # touple

is_sunny = True

