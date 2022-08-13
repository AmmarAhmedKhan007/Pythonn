
# #FUNCTION :

# marks = [55, 88, 90, 70, 80]
# percentage = (sum(marks)/500)*100                   # SUM is a builtin function
# print (percentage)


# #SYNTAX:

# # def func1 ():
# #     print ("func1")


# #QUIck QUIZ: program to greet a user with "GOOD DAY" using functions


# def greet (name):
#     print ("GOOD DAY : " + name)

# # def mySum(num1, num2):            # function with arguments
#     # return (num1+num2)        

# greet ("HARRY")
# # s = mySum(5, 25)
# # print (s)


# # DEFAULT ARGUMENTS

# def greet (name = "STRANGER"):
#     print ("GOOD DAY : " + name)
# # greet ("HARRY")
# greet ()

# #practice

# def ammar():
#     a="hello ammar","how are you"
#     print (a)
# ammar()


#Function with if,elif,else statement



def Ammar():
    name = input("Enter your Name")
    MARKS = int(input("ENTER YOUR MARKS: "))

    if (MARKS>90):
        print (name,"=  A+")

    elif (MARKS>80):
        print (name,"=  A")

    elif (MARKS>70):
        print (name,"=  B")

    elif (MARKS>60):
        print (name,"=  C")

    elif (MARKS>50):
        print (name,"=  D")

    else:
        print (name,"=  FAIL")
Ammar()