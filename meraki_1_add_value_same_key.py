# Write a program such that the below given dictionaries are
# into a single dictionary and add the values having same key.
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# for i in dic1:
#     if i in dic2:
#         dic2[i]=dic2[i]+dic1[i]
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# Q1.Write a Python program to combine two dictionary adding values
# for common keys.
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
for i in dict1:
    if i in dict2:
        dict2[i]=dict1[i]=+dict2[i]
dict1.update(dict2)
print(dict1)
    