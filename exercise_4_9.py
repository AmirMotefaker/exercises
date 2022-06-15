# Code by @Amir Motefaker
# Exercises Chapter 4 #09

# 9- Write a program that takes the name of the month from the user and tells the user in which season this month is.
# Example If the user enters the month Mordad say Summer

month = input("Input the month (e.g. January, February etc.): ")

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

print("Season is",season)

# output:
# Input the month (e.g. January, February etc.): January
# Season is winter
