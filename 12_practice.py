# Q1: STORE 7 FRUITS IN A LIST ENTERED BY USER


F1 = input ("enter fruit 1")
F2 = input ("enter fruit 2")
F3 = input ("enter fruit 3")
F4 = input ("enter fruit 4")
F5 = input ("enter fruit 5")
F6 = input ("enter fruit 6")
F7 = input ("enter fruit 7")
MyFruitsList = (F1 , F2 ,F3 ,F4 ,F5 ,F6 ,F7)
print (MyFruitsList)



#Q2: ACCEPT MARKS OF SIX STUDENTS AND DISPLAY THEM IN SORTED MANNER

F1 = int(input ("enter marks of student 1: "))
F2 = int(input ("enter marks of student 2: "))
F3 = int(input ("enter marks of student 3: "))
F4 = int(input ("enter marks of student 4: "))
F5 = int(input ("enter marks of student 5: "))
F6 = int(input ("enter marks of student 6: "))

MyMarksList = [F1, F2, F3, F4, F5, F6 ]
MyMarksList.sort()
print (MyMarksList)


#Q3: SUM A LIST

a = [1 ,2 ,3 ,4]
print (sum(a))


#Q4: COUNT A NUMBER OF ZEROS IN TUPLE

a = (1, 0, 5, 55, 0, 6, 0)
print (a.count(0))


a= input("fruit 1 =")
b= input("fruit 2 =")
c= input("fruit 3 =")
total =(a , b , c)
print (total)