dic={'a':[4,8],'b':[4,2],'c':[8,3]}
for i in dic:
    x=dic[i]
    list=[]
    sum=0
    j=0
    while j<len(x):
        sum=sum+x[j]
        j=j+1
    list.append(sum)
    dic[i]=list
print(dic)
dic={1,2,3,4,5}
a={}
sum=0
for i in dic:
    sum=sum+i
# dic=[1,2,3,4,5]
# i=0
# d={}
# while i<len(dic):
#     # d[dic[i]]
#     # sum=sum+1
#     i+=1
# print(d)

