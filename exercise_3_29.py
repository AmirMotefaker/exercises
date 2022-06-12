# Code by @Amir Motefaker
# Exercises Chapter 3 #29

# 29. Using the indexes, access the "hello" element in the list below and change its value to "Python".
#   my_list = [1, [1,2,3], ["hello", "hi", 10], 100]

my_list = [1, [1,2,3], ["hello", "hi", 10], 100]

print(my_list[2][0])
# output
# hello

my_list[2][0] = "Python"
print(my_list)
# output
# [1, [1, 2, 3], ['Python', 'hi', 10], 100]
