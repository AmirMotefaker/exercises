# Code by @Amir Motefaker
# Exercises Chapter 3 #30

# 30 - Make a list that has 5 strings stored in it (custom words)
# - Now add the "today" string to it using the append method.
# - A cut in this list so that the result is the values of indexes two, three and four and
# Save it in a variable. Print the result.
# Using the reverse indexing topic, cut the last two values of the list.

my_list = ["amir", "apple", "hello", "germany", "table"]

my_list.append("today")
print(my_list)
# output:
# ['amir', 'apple', 'hello', 'germany', 'table', 'today']


my_list1 = my_list[2:5]
print(my_list1) 
# output:
# ['hello', 'germany', 'table']

# Reverse Indexing
a= my_list[-2:]
print(a)
# output:
# ['table', 'today']

reversed_list = my_list[::-1]
print(reversed_list)
# output:
# ['today', 'table', 'germany', 'hello', 'apple', 'amir']


slicer = slice(5, 3, -1)
reversed_list1 = my_list[slicer]
print(reversed_list1)
# output:
# ['today', 'table']
