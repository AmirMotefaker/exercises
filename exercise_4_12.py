# Code by @Amir Motefaker
# Exercises Chapter 4 #12

# 12. Write a program that asks the user to choose their "username" and "password".
# Now display the messages face to face in the following modes:
# Note that the program is written in two ways.
#  1- In case only one message from the list below is displayed.
#  2 - The state that each of the following conditions that was established to display the relevant message to the user.
#               Result                               condition
# - If the username and password were the same, say they should not be the same
# - If the password length was less than 8 characters, say it must be at least 8 characters
# - If the length of the password was more than 20 characters, say that its length can be a maximum of 20 characters
# If the length of the "username" was less than 4, it should say that its length should be at least 4
# In all wing modes say the entries are correct and "username" and "password" are saved.
# (Note: In the next chapter we will learn how to give the user a second chance to re-enter their information in each of the above cases. And the program ends)

user_name = str(input("Enter UserName :"))
password_user = str(input("Enter Password :"))

if (user_name == password_user):
    print("They should not be the same.")
elif (len(password_user) < 8):
    print(("Password must be at least 8 characters."))
elif (len(password_user) > 20):
    print(("The maximum password length can be 20 characters."))
elif (len(user_name) < 4):
    print(("Username length must be at least 4."))
else:
    print("Entries are correct and 'username' and 'password' are saved.")


# Output:
# Enter UserName :amir
# Enter Password :dfsfsafs6a75fasd8fsafsaf
# The maximum password length can be 20 characters.

# Output:
# Enter UserName :amir
# Enter Password :ali
# Password must be at least 8 characters.
