# Code by @Amir Motefaker
# Exercises Chapter 3 #25

# 25. Make a list that contains the numbers 19, 18, 102, -4, and 0, respectively.
# - In the line after defining the list, write a code that adds the number 54 to the list.
# - Do the previous thing in two different ways. 
# (Tips: A method using one Is one of the list methods and the other method is by adding two lists together)
# - Print the length of this list using the appropriate function.
# - Print indices 2 and 0.
# - Make a slice of the list that includes indexes 1, 2, and 3.

a = ['19', '18', '102', '-4', '0']

a.append("54")
print(a)

a = ['19', '18', '102', '-4', '0']
print(a + ["54"])


print(len(a))

print(a[0], a[2])

b = [a[1], a[2], a[3]]
print(b)

# Output
# ['19', '18', '102', '-4', '0', '54']
# ['19', '18', '102', '-4', '0', '54']
# 5
# 19 102
# ['18', '102', '-4']


# Solution 2
my_list = ['19', '18', '102', '-4', '0']

# my_list.append(54)
my_list += [54]

print(len(my_list)) # len => lenght

print (my_list[1:4])

print(my_list[:4] + my_list[4:])

print(my_list)

# Output
# 6
# ['18', '102', '-4']
# ['19', '18', '102', '-4', '0', 54]
# ['19', '18', '102', '-4', '0', 54]
