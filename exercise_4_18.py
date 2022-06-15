# Code by @Amir Motefaker
# Exercises Chapter 4 #18

# 18. Write a program that takes a word from the user and displays
# its middle letter. If the length of this string is odd then show 
# the middle letter and if its length is even then show the middle two letters.
# Example for abc show the letter b and for abcd show the letters bc to the user.


name = input("Enter your name - ")
 
def middle_charracters(name):
   return name[(len(name)-1)//2:(len(name)+2)//2]
 
print(middle_charracters(name))


# Output:
# Enter your name - dsad
# sa


# Output:
# Enter your name - fdsfdfa
# f
