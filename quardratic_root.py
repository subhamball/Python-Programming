#Write a program that takes as input the coefficients of the quadratic equation ax2 + bx
#+ c = 0 and prints if the roots are complex or real.

a = int(input())
b = int(input())
c = int(input())

discriminant = b*b + 4*a*c;

if(discriminant < 0):
    print("rootsare complex")
else:
    print("roots are real")
    