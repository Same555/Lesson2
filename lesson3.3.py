#!/usr/bin/python

mylist = []

n = int(input("Add array size \n"))
for i in range(0, n):
    temp = int(input("Enter number to array:\n"))
    mylist.append(temp)

print(mylist)
x = int(input("Please add another number:\n"))
for i in range(4, n):
    if mylist[i] < 5:
        mylist[i] = mylist[i] + x
    elif 6 <= mylist[i] <= 10:
        mylist[i] = mylist[i] * x
    elif mylist[i] > 10:
        mylist[i] = mylist[i] ** x
print(mylist)