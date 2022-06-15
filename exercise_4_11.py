# Code by @Amir Motefaker
# Exercises Chapter 4 #11

# 11. Write a program that checks if the input word is "palindrome".
# It is a word for palinderm that is read aloud from beginning to end.
#   For example, the word mom or madam is read the same way from the beginning to the end.
# - If the word is like this, then the sentence Palindrome is This should be displayed
# - If the word is not like this then say Palindrome not is This is displayed.
# (Note: Try to write the program in such a way that it is not case sensitive.
#    For example, the word mom and Mom are both palindromes.)

string = input(("Enter a string:"))

if(string == string[::-1]):
      print("This is Palindrome")
else:
      print("This is not Palindrome")

# output:
# Enter a string:amir
# Not a palindrome

# output:
# Enter a string:mom
# The string is a palindrome
