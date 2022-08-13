# SYNTAX: if(cond 1):                         --> if cond 1 is true
#             print ("yes")
#         elif (cond 2):                      --> if cond 2 is true 
#             print ("no")
#         else:                               --> otherwise
#             print ("maybe")



a =50

# 1. IF-ELIF-ELSE ladder in PYTHON:

if(a>5):
    print ("the value of a is greater than 5")
elif(a>10):                                                 #we use multiple elif in it
    print ("the value of a is greater than 10 ")
else:
    print ("the value is not greater than 5 and 10")



# 2. MULTIPLE IF STatements

# if(a>5):
#     print ("the value of a is greater than 5")
if(a>10):                                              
    print ("the value of a is greater than 10 ")
elif(a>55):
    print ("the value of a is greater than 55")
else:
    print ("the value is not greater than 5 and 10")

print ("done")


#CODE example

a = 20
if (a>5):
    print ("GREATER")
else:
    print ("LESSER")


#QUICK QUIZ

a = int(input ("enter your age:"))
if (a>=18):
    print ("YES")
else:
    print ("NO")



