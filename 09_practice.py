# Q1: PRINT GOOD MORNING TO THE USER

name = input("enter your name")
print ("GOOD MORNING, " + name)


#Q2: REPLACE 

letter = '''Dear <|NAME|>
        you are selected!
        <|DATE|>'''
name = input("enter your name")
date = input("enter date/n")
letter = letter.replace ("<|NAME|>", name)        # use replace function
letter = letter.replace ("<|DATE|>", date)  
print (letter)     