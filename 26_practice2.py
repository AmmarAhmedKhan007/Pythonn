#Q2: PRogram to convert fahernheit to celcius

def farh(cel):
    return (cel * (9/5) + 32)

c = 45
f = farh(c)
print ("fahrenheit temp is: " + str(f))



#Q3: program to print following patterm

n = 6 
for i in range(n):
    print("*" * (n-i))  