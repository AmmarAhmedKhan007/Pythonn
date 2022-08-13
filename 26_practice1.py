# Q1: Using function to find greatest of three numbers

def maximum (num1, num2, num3):
    if(num1>num2):
        if (num1>num3):
            return num1
        else:
            return num2
    else:
        if(num3>num2):
            return num3
        else:
            return num2

m = maximum(55, 88, 77)
print("THE VALUE OF MAXIMUM IS: " + str(m))    