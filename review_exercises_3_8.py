# Code by @Amir Motefaker
# Review Exercises Chapter 3 #8

# 8. Name the types of data in Python and give an example for each.

# Python Numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


# Python List

a = [1, 2.2, 'python']

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

a = [1, 2, 3]
a[2] = 4
print(a)


# Python Tuple

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
#t[0] = 10


# Python Strings

s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
#s[5] ='d'


# Python Set

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

a = {1,2,2,3,3,3}
print(a)


# Python Dictionary

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
#print("d[2] = ", d[2])
