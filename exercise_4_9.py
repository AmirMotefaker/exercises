# Code by @Amir Motefaker
# Exercises Chapter 4 #09

# 9- Write a program that takes the name of the month from the user and tells the user in which season this month is.
# Example If the user enters the month Mordad say Summer

# month = input("Input the month (e.g. January, February etc.): ")

# if month in ('January', 'February', 'March'):
# 	season = 'winter'
# elif month in ('April', 'May', 'June'):
# 	season = 'spring'
# elif month in ('July', 'August', 'September'):
# 	season = 'summer'
# else:
# 	season = 'autumn'

# print("Season is",season)

# output:
# Input the month (e.g. January, February etc.): January
# Season is winter


# Solution 2 - CodingYar
month_name = input('Enter the month name: ')
month_name = month_name.lower()
months = ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad','shahrivar', 'mehr', 'aban', 'azar', 'dey', 'bahman', 'esfand']
seasons = ['spring', 'summer', 'autumn', 'winter']

result = ''

if month_name in months:
    if month_name in months[:3]:
        result = seasons[0]
    elif month_name in months[3:6]:
        result = seasons[1]
    elif month_name in months[6:9]:
        result = seasons[2]
    else:
        result = seasons[3]

else:
    result = 'Incorrect was input'

print(result)


# output:
# Enter the month name: mehr
# autumn

# output:
# Enter the month name: sadasdadsa
# Incorrect was input
    
    
