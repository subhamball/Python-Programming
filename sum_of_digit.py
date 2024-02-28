#Write a program that takes a three-digit integer as input and prints the sum of its
#digits.

number = int(input())
sum = 0
while(number>0):
    sum += number % 10;
    number = number // 10;

print(sum)