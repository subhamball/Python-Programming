#Write a program that takes two integers a and b as input and displays whether a < b,
#a = b, or a > b.
number1 = int(input())
number2 = int(input())

if(number1>number2):
    print("number1 > number2")
elif(number1<number2):
    print("number1 < number2")
else:
    print("number1 = number2")