# Code by @Amir Motefaker
# Exercises Chapter 4 #07

# 7. Write a program that first defines a list of numbers.
#   (Only numbers exist in the list have)
#   - Sort the list first. Then calculate the average of the 
#       largest member of the list and the smallest member of the list.
#   - Then check if this number is bigger or smaller than the middle
#       number in the list and report the result to the user.
#  (Calculate the middle number with the logic of exercise number 5)

# my_list = [1, 3 , 6, -1, 241, 16, -49]

# my_list.sort()
# print(my_list)
# # output:
# # [-49, -1, 1, 3, 6, 16, 241]

# max_my_list = max(my_list)
# print(max_my_list)
# # output:
# # 241

# min_my_list = min(my_list)
# print(min_my_list)
# # output:
# # -49

# average_max_min = (max_my_list + min_my_list) / 2
# print("Average Max and Min =", average_max_min)
# # output:
# # Average Max and Min = 96.0


# middle_number = int(len(my_list) / 2)
# print(middle_number)
# # output:
# # 3


# if average_max_min > middle_number:
#     print("Average Number is bigger than middle number.")
# elif average_max_min < middle_number:
#     print("Average Number is lower than middle number.")

# else:
#     print("Average Number is equal middle number.")

# output:
# Average Number is bigger than middle number.



# Solution 2 - CodingYar
list_of_numbers = [1,5,3,7,8,2]

list_of_numbers.sort()

max_number = list_of_numbers[-1]
min_number = list_of_numbers[0]

avg = (max_number + min_number) / 2

#######
middle_num_of_list = 0

list_length = len(list_of_numbers)

if list_length % 2 == 1:
    my_index = int((list_length - 1) / 2)
    #print(type(my_index))
    middle_num_of_list = list_of_numbers[my_index]
else:
    my_second_index = int(list_length / 2)
    middle_average = (list_of_numbers[my_second_index] + list_of_numbers[my_second_index - 1]) / 2
    middle_num_of_list = middle_average
#######


if avg > middle_num_of_list:
    print('Average Number is -bigger- than middle number.')
else:
    print('Average Number is -lower- than middle number.')


# output:
# Average Number is -bigger- than middle number.
