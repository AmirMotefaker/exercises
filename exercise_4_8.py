# Code by @Amir Motefaker
# Exercises Chapter 4 #08

# 8. Write a program that takes the name of the month from the user. 
# Then display the number of days in that month to the user.
# Example If the user enters the month Azar then print the number 30.

# month = str(input("Enter month: (f, o, k, t ,mo ,s, me, ab, az, d, b, e) "))

# if month == "f" or "o" or "k" or "t" or"mo" or "s":
#     print("31")
# elif month == "me" or "ab" or "az" or "d" or "b":
#     print("30")

# else:
#     print("29")


# output:
# Enter month: (f, o, k, t ,mo ,s, me, ab, az, d, b, e)me
# 31


# Solution 2 - CodingYar
# month_name = input('Enter month name: ')
# month_name = month_name.title()
# # aZAR Azar aZar azar AzAr AZAR

# months = {
#     'Farvardin': 31,
#     'Ordibehesht': 31,
#     'Khordad': 31,
#     'Tir': 31,
#     'Mordad': 31,
#     'Shahrivar': 31,
#     'Mehr': 30,
#     'Aban': 30,
#     'Azar': 30,
#     'Dey': 30,
#     'Bahman': 30,
#     'Esfand': 29
# }

# if month_name in months.keys():
#     print(months[month_name])
# else:
#     print('Incorrect input')



# Solution 3 - CodingYar
month_name = input('Enter month name: ')
month_name = month_name.lower()

first_6_months = ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad','shahrivar']
if month_name in first_6_months:
    print(31)
else:
    if month_name == 'esfand':
        print(29)
    else:
        print(30)

