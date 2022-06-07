# Code by @Amir Motefaker
# Review Exercises Chapter 3 #11

# 11. Write a program that takes a number from the user
# as the radius of the circle and calculates the two 
# values of the circumference and the area of the circle.

r = int(input("Enter r :"))
pi = 3.14

# masahat: pi * r * r
masahat = pi * (r ** 2)

# mohit: (r * 2) * pi
mohit = pi * (2 * r)

print(masahat, mohit)
