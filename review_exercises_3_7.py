# Code by @Amir Motefaker
# Review Exercises Chapter 3 #7

# 7. What methods of strings did we study? Describe the use of each.
# • What is the meaning of place-in methods?

my_str1 = "Hadi"

print(my_str1.upper())
print(my_str1.lower())
print(my_str1.capitalize())

my_str2 = "10,12,hello,19"

print(my_str2.split(','))
print(my_str2.split('o'))

my_list = [1,6,-1,0,12,45,8]
my_list.sort()  # in-place method

print(my_list)

# # if 
# a = my_list.sort()
# print(a)
# # then output is
# None

my_list = [1,6,-1,0,12,45,8]
my_list.sort()  # in-place method
my_list.reverse()

print(my_list)
