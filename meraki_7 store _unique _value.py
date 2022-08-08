                       

a=[{"first":"1"},{"second": "2"},
{"third": "1"},{"four": "5"},
{"five":"5"},{"six":"9"},{"seven":"7"}]
# b=[]
# i=0
# while i<len(a):
#     for j in (a[i]):
#         if a[i][j]not in a:
#           b.append(a[i][j])
#     i+=1
# print(b)
b=[]
i=0
while i<len(a):
    for j in(a[i]):
        b.append(a[i][j])
    i=i+1
print(b)