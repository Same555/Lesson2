#!/usr/bin/python

name = 'arkady'
str1 = str(input('Please add first string: '))
str2 = str(input('Please add second string: '))
num = int(input('Please add number between 1 and 3 :'))
while int(num < 0 or num > 3):
    if num > 3:
        print("Number is bigger then 3")
    else:
        print("Number is lower then 0")
    num = int(input('Please add number between 1 and 3: '))
if len(str1) > len(str2):
    print(str1)
else:
    print(str2)
if str1 in str2:
    print("Exist")
else:
    print("Not Exist")
if str1 > str2:
    str3 = str1[:num]
    str4 = str2[0]
else:
    str3 = str2[:num]
    str4 = str1[0]
print(str3)
print(str4)
if str1 > str2:
    strname = str1.replace(str4, name)
else:
    strname = str2.replace(str4, name)
print(strname)
strsum = str1 + str2 + strname
strsumnew = strsum.replace(" ", "")
print(strsumnew)
print(strsumnew.count('a'))

