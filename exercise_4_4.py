# Code by @Amir Motefaker
# Exercises Chapter 4 #04

# 4 - Write a program that receives two numbers from the user.
# Then tell the user to enter one of the words plus, minus and multiply.
# If the user enters the first, then the result of the sum of these two
# numbers is displayed to the user. If the user enters the second word
# then the result of the first number minus the second number is displayed 
# and if the user enters the third word then the result of multiplying these two is displayed.
# If the user enters a word other than these three then tell him "the entered word is invalid"

num1 = int(input("Enter Num1 :"))
num2 = int(input("Enter Num2 :"))

operators = str(input("Enter p, mi, mul:(Plus, Minus, Multiply) "))

if operators == 'p':
    print(num1 + num2)
elif operators == 'mi':
    print(num1 - num2)
elif operators == 'mul':
    print(num1 * num2)

else:
    print("The entered word is invalid")


# output:
# Enter Num1 :1
# Enter Num2 :2
# Enter p, mi, mul:(Plus, Minus, Multiply) p
# 3

# output:
# Enter Num1 :1
# Enter Num2 :2
# Enter p, mi, mul:(Plus, Minus, Multiply) mi
# -1

# output:
# Enter Num1 :1
# Enter Num2 :2
# Enter p, mi, mul:(Plus, Minus, Multiply) mul
# 2

# output:
# Enter Num1 :1
# Enter Num2 :2
# Enter p, mi, mul:(Plus, Minus, Multiply) minus
# The entered word is invalid
