# Write a program to remove duplicate keys.
# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# # print(dic)
# a=[]
# b={}
# for val,key in dic.items():
#     if key not in a:
#         a.append(key)
#         b[val]=key
# print(b)

dic=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
i=0
a=[]
while i<len(dic):
    for j in dic[i]:
       if dic[i][j] not in a:
        a.append(dic[i][j])
    i=i+1
print(a)

# dic1=[1,2,3,4]
# dic2["one","two","three" ,"four"]
# a={dic1[i]:dic2[i] for i in range(len(dic1))}
# print(a)