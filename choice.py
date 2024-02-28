#Write a program to select one option from the list and display output accordingly.
#Eg. Please enter your choice:
#1. Check Balance.
#2. View Offers.
#3. Special Recharge.
#Enter ‘0’ to exit.
#(Display some arbitrary sentences for each input, like, “Your balance is Rs. 500”)

print("1 for Check balance")
print("2 for View Offers")
print("3 for special Recharge")
print("choose any one option from this input or enter 0 to exit")

latter = int(input())

while (latter > 0 ):

    if(latter == 1 ):
        print("your balance is 1000")
    elif(latter == 2 ):
        print("No offers for you")
    elif(latter == 3 ):
        print("no special recharge for you")
    
    latter = int(input())

print("you enter 0 to exit")