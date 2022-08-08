# Store the unique letters and their frequency of the letters from 
# the word "MISSISSIPPI" to a dictionary, were the letters are the keys and 
# their frequencies are the values.
# o/p={M':1,'I':4,'S':4,'P':2}
a="MISSISSIPPI"
b={}
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
print(b)

# a="themshingla"
# b={}
# for i in a:
#     if i in a():

