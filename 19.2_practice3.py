''' Q4: program to calculate grades of students .........
    90 - 100   -> A+
    80 - 90    -> A
    70 - 80    -> B
    60 - 70    -> C 
    50 - 60    -> D
        <50    -> FAIL'''

MARKS = int(input("ENTER YOUR MARKS: "))

if (MARKS>90):
    print ("A+")

elif (MARKS>80):
    print ("A")

elif (MARKS>70):
    print ("B")

elif (MARKS>60):
    print ("C")

elif (MARKS>50):
    print ("D")

else:
    print ("FAIL")
