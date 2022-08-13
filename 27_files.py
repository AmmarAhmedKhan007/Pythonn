#READ FILE:

#USE Open Function to read the content os file

f = open ('sample.txt', 'r')        # 'r' use for read data
data = f.read()
print (data)
f.close()


#WRITE FILE:

f = open ('sample.txt', 'r')                        # 'w' use for write data
f.write("Please write this to the file")            # 'a' use for appending
f.close()


# WITH STATEMENT

# with open ('sample.txt', 'r'):
# f.read()
