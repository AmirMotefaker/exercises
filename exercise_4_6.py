# Code by @Amir Motefaker
# Exercises Chapter 4 #06

# 6. Write a program that takes two numbers from the user.
#    It then examines the following conditions.
# Result                                        condition
# If the sum of them is between 18 and 20,    then print the number 20
# If the sum of them is between 15 and 18,    then print the number 18
# If the sum of them is between 10 and 15,    then print the number 15
# If the sum of them is less than 10          then say "You did not get enough score"

# num1 = int(input("Enter Num1:(Number between 0-10)"))
# num2 = int(input("Enter Num2:(Number between 0-10)"))

# if 18 < (num1 + num2) < 20:
#     print("20")
# elif 15 < (num1 + num2) < 18:
#     print("18")
# elif 10 < (num1 + num2) < 15:
#     print("15")

# else:
#     print("You did not get enough score.")


# output:
# Enter Num1:(Number between 0-10)7
# Enter Num2:(Number between 0-10)6
# 15


# output:
# Enter Num1:(Number between 0-10)9
# Enter Num2:(Number between 0-10)10
# 20

# output:
# Enter Num1:(Number between 0-10)5 
# Enter Num2:(Number between 0-10)3
# You did not get enough score.


# Solution 2 - CodingYar
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

sum_of_numbers = num1 + num2

if 18 < sum_of_numbers <= 20:
    print(20)
elif 15 < sum_of_numbers <= 18:
    print(18)
elif 10 < sum_of_numbers <= 15:
    print(15)
elif 0 <= sum_of_numbers < 10:
    print('Failed')
else:
    print('You did not get enough score.')


# Output:
# Enter first number: 5
# Enter second number: 13
# 18

# Output:
# Enter first number: 5
# Enter second number: -2
# Failed

# Output:
# Enter first number: -1
# Enter second number: 0
# You did not get enough score.


