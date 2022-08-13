
# Q1: WRITE A PROGRAM to input 4 numbers by user and print greatest one:

num1 = int(input ("enter num 1: "))
num2 = int(input ("enter num 2: "))
num3 = int(input ("enter num 3: "))
num4 = int(input ("enter num 4: "))

if (num1>num4):
    f1 = num1
else:
    f1 = num4

if (num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print (str(f1) +" is GREATEST")
else:
    print (str(f2) +"is GREATEST")