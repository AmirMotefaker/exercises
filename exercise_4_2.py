# Code by @Amir Motefaker
# Exercises Chapter 4 #02

# 2. Write a program that takes a word from the user. 
# Then tell the user whether the length of the word is even or odd.

# name = str(input("Enter your name: "))

# length_name = len(name)%2

# if length_name == 0:
# 	print(name, "even")
# else:
# 	print(name, "odd")

# output:
# Enter your name: dssad231321
# dssad231321 odd

# output:
# Enter your name: 123456$#%^amTR
# 123456$#%^amTR even



# solution 2 - CodingYar
string_length = len(input('Enter your word :'))

if string_length % 2 == 0:
    print('Even')
else:
    print('Odd')


# output:
# Enter your word :hello
# Odd

# output:
# Enter your word :hi
# Even
