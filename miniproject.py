#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp
#
# Created:     28/12/2022
# Copyright:   (c) hp 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
first = input ("enter first number :")
operator = input("enter operator(+,-,*,/,%):")
second = input("enter second number:")

first = int(first)
second = int(second)

if operator =="+":
    print(first + second)
elif operator =="-":
    print(first - second)
elif operator =="*":
    print(first * second)
elif operator =="/":
    print(first / second)
elif operator =="%":
    print(first % second)
else:
    print("invaild statement")