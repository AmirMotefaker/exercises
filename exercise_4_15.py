# Code by @Amir Motefaker
# Exercises Chapter 4 #15

# 15. Change the above program so that the small or large 
# input letter does not make a difference. That is, the letters
# a and A are both vowels, and for this reason the program must
# give the same answer to the input of both.

# my_char = str(input("Enter any character :"))

# if (len(my_char) > 1):
#     print("Input length is more than one.")
# elif ((my_char>='a' and my_char<= 'z') or (my_char>='A' and my_char<='Z')):
#     print(my_char, "is an Alphabet.")
# elif my_char != 0:
#     print(my_char, "is not an Alphabet.")
    
# else:
#     print("The input is correct.")


# output:
# Enter any character :A
# A is an Alphabet.

# output:
# Enter any character :a
# a is an Alphabet.


# Solution 2 - CodingYar
user_char = input('Enter your char: ')

if len(user_char) != 1 :
    print('Input length is more than one')
else:
    if user_char.isalpha():
        if user_char.lower() in ['a', 'e', 'i', 'o', 'u']:
            print('Vowel')
        else:
            print('No Vowel.')
    else:
        print('Must be in alphabetical order.')


# Output:
# Enter your char: A
# Vowel

# Output:
# Enter your char: a
# Vowel

# Output:
# Enter your char: &
# Must be in alphabetical order.
