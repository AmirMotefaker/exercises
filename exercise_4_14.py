# Code by @Amir Motefaker
# Exercises Chapter 4 #14

# 14. Write a program that takes a single letter from the user.
# Apply the conditions of the previous issue first and end the
#    program if the user enters more than one entry.
# But if the input length was one then do the following:
# - First to check whether this single letter is part of the alphabet or not.
# - If it is one of the letters A, the user will be told the same without it.
# - But if it was in the alphabet, check whether it is vowel or not. 
#   Either way, let the user know. (The vowels are the letters o, i, e, a and u.)

# Example If the user enters the letter a, say "the letter is a vowel"
# But if he enters the letter z, say "the letter is silent"


# my_char = str(input("Enter any character :"))

# if (len(my_char) > 1):
#     print("Input length is more than one.")
# elif ((my_char>='a' and my_char<= 'z') or (my_char>='A' and my_char<='Z')):
#     print(my_char, "is an Alphabet.")
# elif my_char != 0:
#     print(my_char, "is not an Alphabet.")
    
# else:
#     print("The input is correct.")


# Output:
# Enter any character :a
# a is an Alphabet.

# Output:
# Enter any character :2
# 2 is not an Alphabet.


# Solution 2 - CodingYar
user_char = input('Enter your char: ')

if len(user_char) != 1 :
    print('Input length is more than one')
else:
    if user_char.isalpha():
        if user_char in ['a', 'e', 'i', 'o', 'u']:
            print('Vowel')
        else:
            print('No Vowel.')
    else:
        print('Must be in alphabetical order.')


# Output:
# Enter your char: p
# No Vowel

# Output:
# Enter your char: *
# Must be in alphabetical order.

# Output:
# Enter your char: asd
# Input length is more than one
