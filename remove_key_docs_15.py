# Write a Python program to remove a key from a dictionary.

# dict1 = {'a': 100, 'b': 200, 'c':300, 'd':400}
# del dict1["a"]
# print(dict1)

dic={'a':[4,8,6],'b':[4,2],'c':[8,3]}
for i in dic:
    list=[]
    x=dic[i]
    sum=0
    
    j=0
    while j<len(x):
        sum=sum+x[j]
        j=j+1
    list.append(sum)
    dic[i]=list
print(dic)