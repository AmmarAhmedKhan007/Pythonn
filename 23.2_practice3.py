# Q6: program to find factorial of a number

num = int(input("ENTER NUMBER"))
factorial = 1
for i in range (1, num+1):
    factorial = factorial * i
print (f"the factorial of {num} is {factorial}")

