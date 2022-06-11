# Code by @Amir Motefaker
# Exercises Chapter 3 #34

# 34 - How to access the value 100 in the following dictionaries?
# - A (simple mode)
# my_dict = {
#  "key1": 100,
#  "key2": 200,
#  "key3": 300
# }

my_dict = {
    "key1": 100,
    "key2": 200,
    "key3": 300
}

a = my_dict["key1"]
print(a)



# - B (list mode inside the dictionary)
my_dict = {
    "mylist": [1,2,45,100],
    "strings": ["hello", "hi"],
    "num": 7,
}

b = my_dict["mylist"][3]
print(b)


# - C (state of a complex value)
my_dict = {
    "mydict": {
        "values": [1,5,'hi',100]
    },
    "strings": ["hello", "hi"],
    "num": 7,
}

c = my_dict["mydict"]["values"][3]
print(c)


# - D (complex mode)
my_dict = {
    "mydict": {
        "inner": {
            "key1": 'hi',
            "key2": [1, 'day', 100, 'bye']
        },
        "inner2": {
            "key1": 8,
            "second": 1
        }
    },
    "strings": ["hello", "hi", 11],
    "num": 10,
}

d = my_dict["mydict"]["inner"]["key2"][2]
print(d)
