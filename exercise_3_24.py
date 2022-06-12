# Code by @Amir Motefaker
# Exercises Chapter 3 #24

# 24. Write a program that stores your name in one variable, your age in another,
# and your favorite programming language in another.
# Now, using the topic of formatting strings, put these three values of variables in the following sentence:
# (Instead of the words 100, Hadi and python, put the values of your variables.)
# My name is Hadi. My age is 100. I love Python.
# • Write the above program once using the format ().
# • Write the above program once using string-fs. (Tip: The same as before the string We wrote an f)

name = "Amir"
age = 43
language = "Python"

# using .format()
print("My name is {0}. My age is {1}. I love {2}".format(name, age, language))
# Output:
# My name is Amir. My age is 43. I love Python


# using f-string
print(f'My name is {name}. My age is {age}. I love {language}. ')
# Output:
# My name is Amir. My age is 43. I love Python



# another solution
print("My name is {a}. My age is {b}. I love {c}".format(b=age, a=name ,c=language))
# Output:
# My name is Amir. My age is 43. I love Python

