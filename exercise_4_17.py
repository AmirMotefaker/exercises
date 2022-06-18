# Code by @Amir Motefaker
# Exercises Chapter 4 #17

# 17. Write the above program in such a way that if the name david
#    is allowed in the participants then if the user enters the name
#    david or even daVId he will still be told "you can log in".
# That is, write the program in such a way that it is not sensitive to uppercase and lowercase letters.

# my_list = ['David', 'elli', 'backy']


# my_char = str(input("Enter name :"))
# if my_char in my_list:
#     print("You can log in.")
# else:
#     print("Nope, You cann't log in.")


# output:
# Enter name :david
# Nope, You cann't log in.


# output:
# Enter name :David
# You can log in.



# Solution 2 - CodingYar
names = ['Ana', 'John', 'david', 'cris', 'elli', 'Baxi']

user_name = input('Enter your name: ')

if user_name.lower() in names:
    print('You can enter.')
else:
    print('No.')


# Output:
# Enter your name: david
# You can enter.

# Output:
# Enter your name: DaviD
# You can enter.

# Output:
# Enter your name: ali
# No.
