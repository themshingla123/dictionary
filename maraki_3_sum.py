# Write a program that prints the sum of values ​​of dictionaries.
# Example :-
# Input :-
# Code Example

# dict = {'data1':100,'data2': -54,'data3': 247}
# def add(dict):
#     a = []
#     for i in dict:
#         a.append(dict[i])
#     b = sum(a)
#     return b
# print(add(dict))

dict1 = {'data1':100,'data2': -54,'data3': 247}
sum=0
for i in dict1:
    sum=sum+dict1[i]
print(sum)

