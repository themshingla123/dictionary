# Take input of name and marks of 10 students and store to a dictionary.
{
'sonu':85,
'Kartik':90,
'Deepak':96,
'Aman':76,
'Somesh':60,
'Umesh':85,
'Amarpal':70,
'Roshan':57,
'Riyaz':98,
'Shabid':56
}
name=["sonu","kartik","deepak","aman","somesh","umesh","amarpal",
"roshan","riyaz","shabid"]
marks=[85,90,96,76,60,85,70,57,98,56]
a={}
i=0
while i<10:
    c=name[i]
    a[c]=marks[i]
    i=i+1
print(a)


