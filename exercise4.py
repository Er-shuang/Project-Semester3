# About age discounts
# Author: Nie Yujin
# Using if elif else

# Input user's age
age = input("Enter your age: ")

# Student discounts
if int(age) <= 19:
    print("You can qualify for student discounts.")
# No discounts
elif 20 <= int(age) <= 54:
    print("You qualify for no age discounts.")
# Senior discounts
else:
    print("You can receive senior discounts.")
