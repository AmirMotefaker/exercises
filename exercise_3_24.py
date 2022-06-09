# Code by @Amir Motefaker
# Exercises Chapter 3 #24

# 24. Write a program that stores your name in one variable, your age in another,
# and your favorite programming language in another.
# Now, using the topic of formatting strings, put these three values of variables in the following sentence:
# (Instead of the words 100, Hadi and python, put the values of your variables.)
# My name is Hadi. My age is 100. I love Python.
# • Write the above program once using the format ().
# • Write the above program once using string-fs. (Tip: The same as before the string We wrote an f)

my_name = "Amir"
age = 43
programming_language = "Python"

# using .format()
print("My name is {0}. My age is {1}. I love {2}".format("Amir", 43, "Python"))


# using f-string
print(f'My name is {my_name}. My age is {age}. I love {programming_language}. ')
