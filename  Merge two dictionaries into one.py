# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# # Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
for i in dict1:
    if i in dict2:
        dict1[i]+dict2[i]
dict1.update(dict2)
print(dict1)



# list1={"a":100,"b":200,"c":300,"d":400}
# list2={"a":200,"b":300,"c":200,"d":500}
# list1= {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# list2 = {'Thirty': 30, 'Fourty': 40, 'Fifty':80 }
# for i in list1:
#     if i in list2:
#         list1[i]+list2[i]
# list1.update (list2)
# print(list1)

