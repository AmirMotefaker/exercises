# Code by @Amir Motefaker
# Exercises Chapter 3 #35

# 35. Create a dictionary that stores your name, your age, 
# and your favorite programming language. 
# Then, using print, write a program that displays all the 
# dictionary keys at once and only the dictionary values once.

my_dict = {
    "name": "amir",
    "age": 43,
    "programming_language": "python"
}

print(my_dict.keys())
# output:
# dict_keys(['name', 'age', 'programming_language'])

print(my_dict.values())
# output:
# dict_values(['amir', 43, 'python'])


print(list(my_dict.keys()))
# output:
# ['name', 'age', 'programming_language']

print(list(my_dict.values()))
# output:
# ['amir', 43, 'python']

print(list(my_dict.items()))
# output:
# [('name', 'amir'), ('age', 43), ('programming_language', 'python')]
