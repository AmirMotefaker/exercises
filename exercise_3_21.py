# Code by @Amir Motefaker
# Exercises Chapter 3 #21

# 21. The following string contains a series of numbers separated by commas.
# Separate these numbers using string methods.
#   my_str = '1,2,3,153,12,56,12,5'

my_str = '1,2,3,153,12,56,12,5'

my_str_out = my_str.split(',')
print(my_str_out)
# output
# ['1', '2', '3', '153', '12', '56', '12', '5']


my_str = '1,2,3,153,12,56,12,5'
print(my_str.split(','))
# output
# ['1', '2', '3', '153', '12', '56', '12', '5']


my_str = '1,2,3,153,12,56,12,5'
print(my_str.split('6'))
# output
# ['1,2,3,153,12,5', ',12,5']
