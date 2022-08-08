a={"themsingla":10,"salu":20,"ariya":30,"nav":40}
b=[]
for i in a:
    b.append(i)
    b.append(a[i])
print(b)

# sum=0
# for i in a.values():
#     sum=sum+i
# print(sum)

# b=[]
# for i in a:
# print(list(a.keys()))

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(b+c)

# user=int(input("enter the number:"))
# i=1
# j=0
# while i<=user:
#     if user%i==0 and user%user==0:
#         j=j+1
#     i=i+1
# if j==2:
#     print("prime no.")
# else:
#     print("not prime no.")