# Code by @Amir Motefaker
# Exercises Chapter 4 #05

# 5. Write a program that tells the user the middle number
#    of a list of numbers defined in a variable.
# Show. To calculate the middle number of a list, two things can be done:
# - If the length of the list is odd, then the middle element is the answer.
# - If the list length is even then display the average of the two middle elements to the user.
# For example for the list [6,5,1] the answer is 5 (middle number)
# But for the list [20,5,4,1] the answer is 5,4 (average 4 and 5 which are the average of the two middle numbers)

list1 = [1, 2, 3, 4, 5]

middle = int(len(list1) / 2) 
print(list1[middle]) 
# output:
# 3



list2 = [1, 2, 3, 4, 5, 6]

first_middle = int(len(list2) / 2) - 1
second_middle = int(len(list2) / 2)  

print(list2[first_middle])  
print(list2[second_middle]) 
# output:
# 3
# 4
