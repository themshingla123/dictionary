user=input("enter the word")
b={}
for i in user:
    if i in b:
       b[i]+=1
    else:
        b[i]=1
print(b)
# sorted=dict(sorted(b.items()))
# for k,l in sorted.items():
#     print('{}:{}'.format(k,l))
# print(sorted)
