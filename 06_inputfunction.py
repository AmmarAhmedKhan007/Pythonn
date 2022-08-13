a = input ("enter your name")
b = input ("enter your age")
print (a)
print (b)


#Q:
# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.

hrs=input("Enter Hour:")
rate=input("Eenter Rate per Hour:")
pay=float(hrs)*float(rate)

print("Pay:", pay)




# hrs = input("Enter Hours:")
# h = float(hrs)
# xx = input("Enter the Rate:")
# x = float(xx)
# if h <= 40:
#  	print( h  * x)
# elif h > 40:
# 	print(40* x + (h-40)*1.5*x)
