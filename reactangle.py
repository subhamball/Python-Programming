#Write a program that takes the length and breadth of a rectangle as input and prints
#its area and perimeter. NOTE: If the inputs are invalid, display an appropriate
#message.
length  = int(input())
breadth = int(input())

print("area is: ",length * breadth)
print("perimeter is: ",2*(length + breadth))