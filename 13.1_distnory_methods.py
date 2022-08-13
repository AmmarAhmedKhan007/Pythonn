myDict = {
    "Fast": "in a quick manner",
    "Ammar": "is khan",
    "Marks": [1 , 4 ,6 ,10]
}
print (myDict.keys())        #print the keys of dictionary
print (myDict.values())     # print values of keys
print (myDict.items())       #kind of list --> print (keys , values)

                            
#update dictionary

updatedict = {
    "you": "are awesome"
}
print (myDict.update(updatedict))
print (myDict)

#get dictionary

print (myDict.get("Ammar"))


#practice 

translate = {"dabba": "box", "aloo": "patato","pankha": "fan"}
print ("Options are", translate.keys())
a = input ("enter the value")
print ("the meaning is",translate[a])