# The factorial of input number
# Author: Nie Yujin
# Using while

# Input a number
num = input("Enter a number: ")

# Return the factorial of that number
i = 1
res = 1
while i <= int(num):
    res = res * i
    i = i + 1

# Print the factorial result
print("The factorial of the input number is: ")
print(res)  
