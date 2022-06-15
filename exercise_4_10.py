# Code by @Amir Motefaker
# Exercises Chapter 4 #10

# 10. Write a program that takes a number from the user. Then show the following modes to the user:
# Note that in the end only one of the following messages should be displayed to the user.
#           Result                                         condition
# If the number was divisible by 3,                 say it is divisible by 3
# If the number was divisible by 5,                 say it is divisible by 5
# If the number was divisible by both 3 and 5,      say it is divisible by 15
# If it is not divisible by any of them,            say it is not divisible by any of them

num = int(input("Enter number :"))

if (num % 3 == 0) and (num % 5 == 0):
    print("The number is divisible by 3,5.")
elif num % 3 == 0:
    print("The number is divisible by 3.")
elif num % 5 == 0:
    print("The number is divisible by 5.")


else:
    print("It is not divisible on any of them.")

# output:
# Enter number :15
# The number is divisible by 3,5.

# output:
# Enter number :21
# The number is divisible by 3.
