a = {1, 3, 5, 7 , 9}              #set is a collection of non repetitive elements
# print (type(a))
print (a)

#EMPTY SET

b = set()
print (type(b))

#ADD method
b.add(5)          #adding 5 in empty set
b.add(10)
# b.add[1 ,2 ,3 ,4]         #we do not add list in the set
b.add((1, 2, 5 ))           #we can add tuple in a list
# b.add({5:4})                #we cannot add dictionary in a set
print (b)

#LEN method

print (len(b))       #print length of a set

#REMOVE method

b.remove(5)         #remove 5 from set b
print (b)

#POP METHOD
 
b.pop()          #remove element is a set 
print (b)

#CLEAR method

b.clear()         #empties the set
print (b)

#UNION and INTERSECTION

b.union({1,5})
b.intersection({1,5})
print (b)

