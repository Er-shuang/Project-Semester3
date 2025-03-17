# The factorial of input number
# Author: Nie Yujin
# Using for

# Input a number
num = input("Enter a number: ")

# Return the factorial of that number
i = 1
res = 1
for i in range(1, int(num) + 1):
    res = res * i

# Print the factorial result
print("The factorial of the input number is: ")
print(res)  

