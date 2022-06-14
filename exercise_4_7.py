# Code by @Amir Motefaker
# Exercises Chapter 4 #07

# 7. Write a program that first defines a list of numbers.
#   (Only numbers exist in the list have)
#   - Sort the list first. Then calculate the average of the 
#       largest member of the list and the smallest member of the list.
#   - Then check if this number is bigger or smaller than the middle
#       number in the list and report the result to the user.
#  (Calculate the middle number with the logic of exercise number 5)

my_list = [1, 3 , 6, -1, 241, 16, -49]

my_list.sort()
print(my_list)
# output:
# [-49, -1, 1, 3, 6, 16, 241]

max_my_list = max(my_list)
print(max_my_list)
# output:
# 241

min_my_list = min(my_list)
print(min_my_list)
# output:
# -49

average_max_min = (max_my_list + min_my_list) / 2
print("Average Max and Min =", average_max_min)
# output:
# Average Max and Min = 96.0


middle_number = int(len(my_list) / 2)
print(middle_number)
# output:
# 3


if average_max_min > middle_number:
    print("Average Number is bigger than middle number.")
elif average_max_min < middle_number:
    print("Average Number is lower than middle number.")

else:
    print("Average Number is equal middle number.")

# output:
# Average Number is bigger than middle number.
