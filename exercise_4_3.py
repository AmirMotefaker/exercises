# Code by @Amir Motefaker
# Exercises Chapter 4 #03

price = int(input("Enter price :"))

if price > 1000:
    print("Too expensive.")
elif 500 < price < 1000:
    print("It is expensive.")
elif 100 < price < 500:
    print("It is normal.")
else:
    print("It is cheap.")

# output:
# Enter price :1001
# Too expensive.

# output:
# Enter price :800
# It is expensive.

# output:
# Enter price :264
# It is normal.

# output:
# Enter price :75
# It is cheap.
