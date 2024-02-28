#Write a program that takes a valid letter grade (S/A/B/C/D/E) as input and prints
#its respective grade point (10/9/8/7/6/4). NOTE: If an invalid letter grade is
#entered, the program should display an appropriate message.

latter = input()

if(latter == 'S' ):
    print(10)
elif(latter == 'A'):
    print(9)
elif(latter == 'B'):
    print(8)
elif(latter == 'C'):
    print(7)
elif(latter == 'D'):
    print(6)
elif(latter == 'E'):
    print(4)
else:
    print("Invalid later grade is entered")
