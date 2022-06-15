# Code by @Amir Motefaker
# Exercises Chapter 4 #16

# 16. Write a program that manages the staff to enter a specific course.
# In this way, the user enters his name. If his name is on the list of 
# participants then he is told to enter. If not then he is told he has no right to enter.
# (Make a list for the list of participants and save some names of your choice in it)

user = str(input("Enter your name :"))

my_list = [Ana, John, Bail, cris, elli, Baxi]

if user == my_list:
    print("Your Welcome.")
else:
    print("You do not have the right to enter.")
