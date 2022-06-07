# Code by @Amir Motefaker
# Review Exercises Chapter 3 #10

# 10. Do the following on a list.
# • Add a variable to the list.
# • Add to the list of three variables.
# • Change the fifth element of the list
# • Replace it with a number.
# • Replace it with a dictionary.
# • Remove the third index from the list and save it in a variable.
# • Sort the list.
# • Reverse the order of the data in the list.
# • Find the largest and smallest values in the list


## • Add a variable to the list.

my_list = [3, 4, 5, 1, 2]

# my_list.append(10)
my_list.extend([100 , 101])  # extend from list
# my_list = my_list + [100, 101]
# my_list += [100, 101]

# print(my_list + ['hello'])

print(my_list)



## • Add to the list of three variables.

my_list = [3, 4, 5, 1, 2]

a = 1
b = 2
c = 3
my_list.extend([a, b, c])

print(my_list)



## • Change the fifth element of the list

my_list = [3, 4, 5, 1, 2]

my_list[4] = 'hello'

print(my_list)


## • Replace it with a number.


my_list = [3, 4, 5, 1, 2]

my_list[3] = 100

print(my_list)


## • Replace it with a dictionary.

my_list = [3, 4, 5, 1, 2]

my_list[4] = {"k1": "v1", "k2": "v2"}

print(my_list)


## • Remove the third index from the list and save it in a variable.

my_list = [3, 4, 5, 1, 2]

a = my_list.pop(2)

print(a)
print(my_list)


## • Sort the list.

my_list = [3, 4, 5, 1, 2]

a = my_list.sort()

print(my_list)


## • Reverse the order of the data in the list.

my_list = [3, 4, 5, 1, 2]

a = my_list.reverse()

print(my_list)


## • Find the largest and smallest values in the list

my_list = [3, 4, 5, 1, 2]


print(max(my_list))
print(min(my_list))
