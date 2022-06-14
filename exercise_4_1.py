# Code by @Amir Motefaker
# Exercises Chapter 4 #01

# 1. Write a program that takes a number from the user.
# Then tell the user whether the number is even or odd. 
# (Tip: Do not forget to convert input to number)

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# output:
# Enter a number: 131
# This is an odd number.

# output:
# Enter a number: 598
# This is an even number.
