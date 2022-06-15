# Code by @Amir Motefaker
# Exercises Chapter 4 #08

# 8. Write a program that takes the name of the month from the user. 
# Then display the number of days in that month to the user.
# Example If the user enters the month Azar then print the number 30.

month = str(input("Enter month: (f, o, k, t ,mo ,s, me, ab, az, d, b, e) "))

if month == "f" or "o" or "k" or "t" or"mo" or "s":
    print("31")
elif month == "me" or "ab" or "az" or "d" or "b":
    print("30")

else:
    print("29")


# output:
# Enter month: (f, o, k, t ,mo ,s, me, ab, az, d, b, e)me
# 31
