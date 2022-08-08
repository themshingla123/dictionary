# dict={"a":[3,2,1],"b":[7,6,5]}
# dict={101:"ram",102:"sham"}
# b={}
# for j in dict:
#     x=dict[j]
#     i=-1
#     c=[]
#     while i>=-len(x):
#         c.append(x[i])
#         i-=1
#     b[j]=c
# print(b)

a={'a':[23,45,34],'b':[12,11,23]}
b={}
for i in a:
    x=a[i]
    sum=0
    j=0
    while j<len(a)+1:
        sum+=x[j]
        
        c=sum/3
        j+=1
    b[i]=c
print(b)



# b=list(a)
# print(b)
# i=0
# while i<len(a):
#     print(b[-1])
#     i=i+1