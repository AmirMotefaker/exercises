# Code by @Amir Motefaker
# Exercises Chapter 3 #41

# 41. What are the total storage capacity of booleans? Give a few examples.

# Booleans represent one of two values: True or False.

# Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Example 3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Example 4
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# Example 5
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
# output:
# YES!



my_boolean1 = True

my_boolean1 = False

is_yesterday_12th = True

are_you_good = False

