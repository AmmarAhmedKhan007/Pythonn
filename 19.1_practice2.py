''' Q2: WRITE A PROGRAM .....student is pass or fail,it require total 40% and at least 33% in 
 each subject to pass. assume 3 subjects ....input from the user.'''

sub1 = int(input("enter marks of first subj: "))
sub2 = int(input("enter marks of secind subj: "))
sub3 = int(input("enter marks of third subj: "))

if (sub1<33 or sub2<33 or sub3<33):
    print ("you are FAIL because you have less than 33% marks in one subject")

elif (sub1+sub2+sub3)/3 < 40:
    print ("youare FAIL because your total percentage is less than 40")

else:
    print ("CONGRATS! YOU ARE PASSED")



# Q3: write a program which find out weather the name is present in alist or not


names = ["ammar","khan","ali","abdullah","hassan","bushra","ayesha"]
name = input("enter the name: ")

if name in names:
    print ("you are present in a list")
else:
    print ("you are not present ")