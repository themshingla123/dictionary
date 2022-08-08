# a="manpreet"
# b=7.0
# c=8
# d=str(b)
# e=str(c)
# print(a,",",d,",",e)


# update meth0ds:
# a={1:2,2:3,3:4}
# # a1={1:0}
# a1={7:8}
# a.update(a1)
# print(a)

# values method():

# a={1:2,2:3,3:4}
# d=a.values()
# print(d)


# a={1:2,2:3,3:4}
# d=a.keys()
# print(d)

# items():

# a={1:2,2:3,3:4}
# a.items()
# print(a)

# get() method..
# a={1:2,2:3,3:4}
# b=a.get()
# print(b)

# # pop():
# a={1:2,2:3,3:4}
# a.pop(3)
# print(a)

# popitem():
# a={1:2,2:3,3:4,7:9}
# # a.popitem()
# # print(a)
# b=a.popitem()
# print(b)


# clear()
# a={1:2,2:3,3:4,7:9}
# a.clear()
# print(a)

# setdefault()
# x=["mango","apple","papaya"]
# y=[20,3,40,50]
# a=zip(x,y)
# b={}
# for i,j in a:
#     if i not in b:
#         b[i]=y
#     else:
#         pass
# print(b)
# print(a.setdefault("ID","no ID"))
# print(a.setdefault(7))
# print(str(a))

# fromkey()
# a={1,2,3}
# b=dict.fromkeys(a,"themsingla")
# print(b)

# a={5:6,4:8,7:3}
# a.copy()
# print(a)
# a={5:6,4:8,7:3}
# a["year"]=19
# print(a)

# p 101:"ram"
#     102:"sham"
#     103:"rhada
# dict={101:"ram",102:"sham",103:"rhada"}
# for i in dict:
#     print(i,":",dict[i])

# dict={3:2,4:5,6:8}
# for i in dict:
#     print("key is",i,"and value is",dict[i])
# dict[7]=2
# print(dict)

# a="themshingla"
# b={}
# for i in a:
#     if i in b:
#         b[i]=+1
#     else:
#         b[i]=1
# print(b)
# b=[]
# for i in dict.values():
#     b.append(i)
# print(max(dict))
# print(min(dict))

# dict={2:5,8:9,6:3}
# a=[]
# for i in dict:
#     a.append(dict[i])
# print(a)

# a="my name is themshingla"
# b=list(a)
# i=0
# while i<len(b):
#      print(b[-1])
# i=i+1
# b=split.a()
# print(b)


# day=int(input("enter the num of days from1 to 7="))
# if day==1:
#     print("monday")
# elif day==2:
#     print("tuesday")
# elif  day==3:
#     print("wednesday")
# elif day==4:
#     print("thursday")
# elif day==5:
#     print("friday")
# elif day==6:
#     print("saturday")
# elif day==7:
#     print("sunday")
# else:
#     print("none")

month=int(input("enter the month no"))
if month==1:
    print("january=31days")
elif month==2:
    print("february=28/29days")
elif month==3:
    print("march=30 days")
elif month==4:
    print("april=31days")
elif month==5:
    print("may=30 days")
elif month==6:
    print("june=31days")
elif month==7:
    print9("jull=30 daysy")
elif month==8:
    print("augest=31days")
elif month==9:
    print("sep=30days")
elif month==10:
    print("oct=31days")
elif month==11:
    print("nov=30days")
elif month==12:
    print("dec=31`days")
else:
    print("none")
    