#!/usr/bin/python

num1 = int(input('Please input First Number: '))
num2 = int(input('Please input Second Number: '))
Sum = num1 + num2
Div = num1 / num2
Mul = num1 * num2
print("Sum is", Sum, '\n' "Multiply is", Mul, '\n' "Divide is", Div)
if num1 == num2:
    print("Equal")
elif num1 > num2:
    print("Biggest Number is", num1)
else:
    print("Biggest Number is", num2)
print("Good Bye")









