# Welcome to Vandyck's Repository.
# This code is a basic code for random password generator.

# install random module in your terminal
# use this command: pip install random

# After installed, use the random module by import
import random

# set password characters option
capital_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
small_letters = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
symbols = "!@#$%^&*()-_+={[}]|:;'<,>.?/"
password_characters = capital_letters + small_letters + numbers + symbols

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
