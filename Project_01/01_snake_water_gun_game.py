import random


def gamewin (comp, you):
    if (comp == you):
        return None
    elif (comp == 'S'):
        if (you == 'W'):
            return False
        elif (you == 'G'):
            return True
    elif (comp == 'W'):
        if (you == 'S'):
            return True
        elif (you == 'G'):
            return False
    elif (comp == 'G'):
        if (you == 'W'):
            return True
        elif (you == 'S'):
            return False

print ("Comp turn: Snake(S) Water(W) or Gun(G)?")
randno = random.randint(1, 3)
if randno == 1:
    comp = 'S'
elif randno == 2:
    comp = 'G'
elif randno == 3:
    comp = 'W'

you = input ("Your turn: Snake(S) Water(W) or Gun(G)?")
a = gamewin (comp, you)

print (f"Comp choose: {comp}")
print (f"You choose: {you}") 

if a == None:
    print ("THE GAME IS TIE")
elif a:
    print ("YOU WIN")
else:
    print ("YOU LOSE")