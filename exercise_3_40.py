# Code by @Amir Motefaker
# Exercises Chapter 3 #40

# 40. What is Tuple? What is the difference with lists? 
# Make a tuple with values of 1, 2 and 3.

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(type(my_tuple))

my_tuple2 = ("1", "2", "3")
print(my_tuple2)
print(type(my_tuple2))

# Difference Between List and Tuple in Python:  
# NO.	    LIST	                                            TUPLE
# 1	    Lists are mutable	                             Tuples are immutable
# 2	    Implication of iterations is Time-consuming	     The implication of iterations is comparatively Faster
# 3	    The list is better for performing operations,
#          such as insertion and deletion.	             Tuple data type is appropriate for accessing the elements
# 4	    Lists consume more memory	                     Tuple consume less memory as compared to the list
# 5	    Lists have several built-in methods	             Tuple does not have many built-in methods.
# 6	    The unexpected changes and errors are more
#          likely to occur	                             In tuple, it is hard to take place.

my_list = ['an', 'example', 'of', 'a', 'list']
my_tuple = ('this', 'is', 'an', 'example', 'of', 'tuple')

