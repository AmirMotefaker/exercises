# Code by @Amir Motefaker
# Review Exercises Chapter 3 #12

# 12. Print the above query values using formatting strings.

r = int(input("Enter r :"))
pi = 3.14

# masahat: pi * r * r
masahat = pi * (r ** 2)

# mohit: (r * 2) * pi
mohit = pi * (2 * r)

# print('masahat: {}, mohit: {}'.format(masahat, mohit))

# f-string:
print(f'masahat {masahat}, mohit: {mohit}')
