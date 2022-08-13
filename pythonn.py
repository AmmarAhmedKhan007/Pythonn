# import pyttsx3


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print (voices)

# def speak(audio):
#     pass





a= int(input ("enter your age"))
if (a>18):
    print ("yes")
elif (a==18):
    print ("satisfied")
else:
    print ("no")


''' Q4: program to calculate grades of students .........
    90 - 100   -> A+
    80 - 90    -> A
    70 - 80    -> B
    60 - 70    -> C 
    50 - 60    -> D
        <50    -> FAIL'''

marks = int (input ("Enter Your Marks"))
if (marks>90):
    print ("A+")
elif (marks>80):
    print ("A")
elif (marks>70):
    print ("B")
elif (marks>60):
    print ("C")
elif (marks>50):
    print ("D")
else:
    print ("YOU ARE FAIL")

print ("CONGRAGULATIONS")


sub1 = int (input("Enter your marks"))
sub2 = int (input("Enter your marks"))
sub3 = int (input("Enter your marks"))
if (sub1<33 or sub2<33 or sub3<33):
    print ("You are Fail")
elif (sub1+sub2+sub3)/3 <40:
    print("you are fail shds ds")
else:
    print ("you are pass")