# Code by @Amir Motefaker
# Exercises Chapter 4 #13

# 3. Write a program that tells the user to "enter a letter"
# Because we want a letter from the user, its length must be one.
#   If the user input is longer than one, tell the user that "input
#   length is more than one" and the program will end. Otherwise say "input is correct"

# letter = str(input("Enter Letter :"))

# if (len(letter) > 1):
#     print("Input length is more than one.")
# else:
#     print("The input is correct.")

# output:
# Enter Letter :sd
# Input length is more than one.

# output:
# Enter Letter :a
# The input is correct.



# Solution 2 - CodingYar
# user_char = input('Enter your char: ')

# if len(user_char) > 1 or len(user_char) ==0:
#     print('Input length is exactly than one.')
# else:
#     print('Good.')


# Solution 3 - CodingYar
user_char = input('Enter your char: ')
#len(user_char) > 1 or len(user_char) ==0
if len(user_char) != 1 :
    print('Input length is exactly than one.')
else:
    print('Good.')

# Output:
# Enter your char:
# Input length is exactly than one.

# Output:
# Enter your char: a
# Good.

