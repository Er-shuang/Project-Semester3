# Guess a Random Number
# Author: Nie Yujin
# Using random

import random

# select a random number between 10 and 20
random_num = random.randint(10, 20)

print("Here is the random number: ")
print(random_num)

found = 0

# guess a number 
number = input("Guess and enter a number: ")

while found == 0:
    if int(number) == random_num:
        found = 1
    else:
        number = input("Enter a number again: ")

print("Congratulation! You guess it!!!")
