a={5:10,2:8,1:7}
b=[]
for i in a:
    b.append(i)
    b.append(a[i])
print(b)