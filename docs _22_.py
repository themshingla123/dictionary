# Write a Python program to create and display all combinations of letters, 
# selecting each letter from a different key in a dictionary. Go to the editor
# a={'1'['a','b'], '2'['c','d']}
# # ac
# # ad
# # bc
# b=list(a.value())
# for i in b[0]:
#     for j in a[i]:
#         print(i+j)

d={101:"ram",102:"sham"}
e={}
for i in d:
    e[d[i]]=i
print(e)