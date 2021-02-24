# Welcome to Vandyck's Repository.
# This code is a basic code for random password generator.

# if your python does not have these modules, install in your terminal
# use this command: pip install random, pip install string

# After installed, utilize the modules
import random as rd
import string as st

# set password characters option
password_characters = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation

# password option and length defining
password_1 = ""
password_2 = ""
password_length = input("Length of password:")

# generating password randomly based on length that users request for
a = 0
while a < int(password_length):
    password_1 = password_1 + random.choice(password_characters)
    a = a + 1

a = 0
while a < int(password_length):
    password_2 = password_2 + random.choice(password_characters)
    a = a + 1

print("\nThis is your password options, choose your password\n" + "1. " + password_1 + "\n2. " + password_2)
# giving options to users to choose the password they want based on their preference from the 2 options generated


def password_option():
    choice = input("\nWhich password do you prefer to use?\nEnter your choice by number: ")
    if choice == str("1"):
        print("You have chosen option number 1, your password is: " + password_1)
        return choice
    elif choice == str("2"):
        print("You have chosen option number 2, your password is: " + password_2)
        return choice
    else:
        print("Your choice is invalid. Please choose it again.")
        return password_option()


choice = password_option()
# data validation section that make sure the users enter the correct password


def password_validation(choice=choice):
    valid = input("\nPlease re-enter your password to verify: ")
    if valid == password_1 and choice == str("1") or valid == password_2 and choice == str("2"):
        return" ***** Congratulations, you had entered Vandyck's server. ***** "
    else:
        print("This is not a valid password. Please try again.")
        return password_validation()


print(password_validation())
