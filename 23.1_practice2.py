# Q4: to find weather a given number is prime or not

num = int(input("enter the number"))
prime = True

for i in range (1, num):
    if (num%i == 0):
        prime = False
        break

if prime:
    print ("PRIME")
else:
    print ("NOT PRIME")



# Q5: find the sum of first n natural numbers using while loop

#  num = [1, 2, 3, 4, 5, n,]
#  i = 1
#  while (i+num):
#     print (num[i])
#     i = i + 1
