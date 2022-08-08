# Q30.Write a Python program to remove spaces from dictionary keys.
# Original:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 

# d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# e={}
# for i,j  in d.items():
#     c=i.split()
#     e["".join(c)]=j
# print(e)
# d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# e={}
# for i,j  in d.items():
#     for x in " ":
#         i=i.replace(x,"")
#     e[i]=j
# print(e)

# a=[1,2,3,4,5,6]
# b=[]
# i=0
# j=-1
# while i<len(a)/2:
#     b.append(a[j])
#     b.append (a[i])
#     i=i+1                                                   
#     j=j-1
# print(b)

dict={1:"value1",2:"value2",3:"value3"}
for i in dict:
    print("key is",i,"and value is",dict[i])

    