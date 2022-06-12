# Code by @Amir Motefaker
# Exercises Chapter 3 #38


# 38. Consider the following dictionary.
# person_details = {
#  "name": "Ana",
#  "age": 28,
#  "languages": ["Python", "Java", "C"]
#  }
# - With what code can we get the name of the person from the following dictionary?
# - With what code can we get the languages list of the above question?
#    That is, with what code should we tell Python to return the list in front of the above dictionary languages?
# - How can we access the third element of the languages list?

 
person_details = {
    "name": "Ana",
    "age": 28,
    "languages": ["Python", "Java", "C"]
}


print(person_details["name"])

print(person_details["languages"])

print(person_details["languages"][2])
# output:
# Ana
# ['Python', 'Java', 'C']
# C
