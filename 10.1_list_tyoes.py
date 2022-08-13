#sort list

l1 = [ 1,3,4,7,77,34,2,0]
l1.sort()
print (l1)

#reverse list

l2 = [ 1,3,4,7,77,34,2,0]
l2.reverse()
print (l2)

#Append list   #ADD AT THE END OF LIST

l3 = [ 1,3,4,7,77,34,2,0]
l3.append(100)            #add 100 at the end of list
print (l3)


#insert list
l4 = [ 1,3,4,7,77,34,2,0]
l4.insert(2 ,99)         #this will insert 99 in index 2
print (l4) 


#pop list
l5 = [ 1,3,4,7,77,34,2,0]
l5.pop(2)                # will delete element at index 2
print (l5)


#remove list
l6 = [ 1,3,4,7,77,34,2,0]
l6.remove(77)           #will remove 77 from the list
print(l6)