# Q1: PRINT multiplication table of given number using for loop

num = int(input("ENTER NUMBER"))
for i in range (1, 11):
    print(f"{num}X{i}={num*i}")                                      # use F string


#Q2: program to greet all the persons names stored in list l1 and wich starts with A:

l1 = ["Ammar", "Hassan", "Ali", "khan"]
for name in l1:
    if name.startswith("A"):
        print("WELCOME "  + name)


#Q3: Q1 using while loop


num = int(input("ENTER NUMBER"))
i = 1
while i<11:
    print (f"{num}X{i}={num*i}")
    i = i + 1
