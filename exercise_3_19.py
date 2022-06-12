# Code by @Amir Motefaker
# Exercises Chapter 3 #19

# 19 - Consider the following string.
#   my_str = 'CodingYar.com'
# • Select the letter n in this string, using indexing and display it.
# • Select and display the letter m in two different ways.
# • Using slicing, show the top string upside down.

my_str = 'CodingYar.com'

print(my_str[4])
# output
# n

print(my_str[-9])
# output
# n


print(my_str[12])
# output
# m
print(my_str[-1])
# output
# m


print(my_str[6:9])
# output
# Yar

print(my_str[6:9:1])
# output
# Yar


print(my_str[::-1])
# output
# moc.raYgnidoC

print ("".join(reversed(my_str)))
# output
# moc.raYgnidoC

