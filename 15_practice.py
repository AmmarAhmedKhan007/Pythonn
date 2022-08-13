
# Q1: PROGRAM TO CREATE A DICTIONARY OF HINDI WORDS AND TRANSLATE IT
#  PRIVIDE USER WITH AN OPTION TO LOOK IT UP:

myDict = {
    "panka": "fan",
    "dabba": "box",
    "laila": "item",
}
print ("options are:", myDict.keys())
a = input ("enter the word")
print ("the meaning of word is:",myDict[a])



# Q2: PROGRAM TO INPUT 8 NUMBERS FROM USER AND DISPLAY ALL THE UNIQUE NUMBERS:

a = int(input ("enter the number 1"))
b = int(input ("enter the number 2"))
c = int(input ("enter the number 3"))
d = int(input ("enter the number 4"))
e = int(input ("enter the number 5"))
f = int(input ("enter the number 6"))
g = int(input ("enter the number 7"))
h = int(input ("enter the number 8"))

T = {a, b, c, d, e, f, g, h}
print (T)


#Q3: CAN WE HAVE A SET WITH 18 int AND "18"str AS A VALUE IN IT

a = {18, "18"}
print (a)


# Q4: WHAT WILL BE THE LENGT OF SET S

S = {20, 21.2, "45"}
print (len(S))


#Q5: S={}  what is the type of S

s = {}
print (type(s))

