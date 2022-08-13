import random
randno = random.randint(1, 5)                   # it automatically generate random number from 1 to 5

userguess = int(input("ENTER THE NUMBER:" ))

if (userguess == randno):
    print ("YOU GUESS RIGHT NUMBER ")
elif (userguess > randno):
    print ("YOU ENTER GREATER NUMBER ")
elif (userguess < randno):
    print ("YOU ENTER SMALLER NUMBER")
