#Write a program that takes three integers as input and prints their maximum values.
number1 = int(input())
number2 = int(input())
number3 = int(input())

if(number1>number2):
    if(number1>number3):
        print(number1)
    else:
        print(number3)
elif(number1<number2):
    if(number2>number3):
        print(number2)
    else:
        print(number3)
else:
    print("all are equal number")