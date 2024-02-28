#Write a program that takes two 5-letter words as input and finds the sum of the
# distance between the respective characters of these words. Examples are given in the
# table below:
# Input: abcde
# abdfe
# Distance: 0-0-1-2-0
# Output: 3 (0+0+1+2+0)
# Input: pqxzy
# qpyax
# Distance: 1-1-1-25-1
# Output: 29 (1+1+1+25+1)

print("enter two 5 latter words")

latter1 = input()
if(len(latter1) !=5 ):
    print("you entered word1 is not length 5")

latter2 = input()
if(len(latter1) !=5 ):
    print("you entered word2 is not length 5")

