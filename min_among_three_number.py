#Write a program that takes three integers as input and prints the minimum (of the
#three values).

number1 = int(input())
number2 = int(input())
number3 = int(input())

if(number1>number2):
    if(number2>number3):
        print(number3)
    else:
        print(number2)
elif(number2>number1):
    if(number1>number3):
        print(number3)
    else:
        print(number1)
else:
    print("all are equal number")