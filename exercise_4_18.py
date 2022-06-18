# Code by @Amir Motefaker
# Exercises Chapter 4 #18

# 18. Write a program that takes a word from the user and displays
# its middle letter. If the length of this string is odd then show 
# the middle letter and if its length is even then show the middle two letters.
# Example for abc show the letter b and for abcd show the letters bc to the user.


# name = input("Enter your name - ")
 
# def middle_charracters(name):
#    return name[(len(name)-1)//2:(len(name)+2)//2]
 
# print(middle_charracters(name))


# Output:
# Enter your name - dsad
# sa


# Output:
# Enter your name - fdsfdfa
# f


# Solution 2 - CodingYar
user_input = input('Enter your word: ')
# abc    len:3   middle_index: 1
# abcd   len:4   middle_index: 1,2

word_len = len(user_input)

if word_len == 0:
   print('Lenght is zero.')
else:
   if word_len % 2 == 1:
      index = int((word_len - 1)  / 2)
      print(user_input[index])
   else:
      index = int(word_len / 2)
      print(user_input[index-1:index+1])


# Output:
# Enter your word: abc
# b

# Output:
# Enter your word: abcd
# bc

# Output:
# Enter your word: 
# Lenght is zero.
