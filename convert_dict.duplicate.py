# Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]dic = {'list1': [4, 7, 10, 20], 
a=[]
dict= {'list1': [4, 7, 10, 20], 
      'list2': [7, 16, 9, 10], 
      'list3': [13, 10, 4, 8], 
      'list4': [7, 20, 6, 11]}
Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]
for i in dict:
    a.extend(dict[i])
j=0
b=[]
while j<len(a):
    if a[j] not in b:
        b.append(a[j])
    j+=1
b.sort()
print(b)
