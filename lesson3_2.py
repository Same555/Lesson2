#!/usr/bin/python

def listsum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


def getlistsum():
    numbers = []
    while True:
        inp = int(input("Please enter numbers: \n"))
        numbers.append(inp)
        if listsum(numbers) > 30 or inp > 10:
            return listsum(numbers)


print(getlistsum())