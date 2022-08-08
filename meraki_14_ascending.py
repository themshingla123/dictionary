# Write a program to sort a dictionary in ascending 
# or descending according to its values .
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in a:
#     for j in a:
#         if a[j]<a[i]:
#             a[j],a[i]=a[i],a[j]
#         if a[i]< a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# p=sorted(a.values())
# # print(p)
# b={}
# for i in p:
#     for j in a.keys():
#         if a[j]==i:
#             b[j]=i
# print(b)

# dict={8:7,6:8,8:4}
# for i in dict:
#     print(dict)

# dict={101:"ram",102:"sham",103:"rhada"}
# for i in dict:
#     print(i,':',dict[i])

# dict={101:"ram",102:"sham",103:"rhada"}
# for i in dict:
#     print('key is',i,'and value is',dict[i])

a="my name is themsingla"
b=a.split()
d={}
i=0
while i<len(b)-1:
    i+=1
c=b[i]
d[b[i]]=1
print(d)