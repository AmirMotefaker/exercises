# Code by @Amir Motefaker
# Exercises Chapter 3 #37

# 37. Write a program that asks the user questions three times
# (using input) and the user must answer three times.
# The first question is "What is your name?" 
# The second question is "In what country Do you live? ”
# And third,“ How old are you? ”
# Now display all three user responses you received from the user and saved in different variables, in the following sentence:
# Hi User Name .You live in Country Name .Your age is User Age.
# Instead of three Persian words (gray color), put the appropriate variable value.

name = input("What is your name :")
country = input("Where country do you live in :")
age = input("How old are you :")

print(f"Hi, {name}. You live in {country}. Your age is {age}")
