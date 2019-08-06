# -*- coding: utf-8 -*-
"""
@author: samuel
"""

minNum = 4

print("greetings! i will go through a range of natural numbers and declare their primality!")

maxNum = int(input("enter max pl0xXz!!!11: "))

for currentNum in range(minNum,maxNum+1): #go thru a list of ints
    
    #print(currentNum,'currently. ', end='') #debug current int
    numFac = 0
    if currentNum % 2 == 0 or currentNum % 3 == 0:
        print(currentNum,'is composite.')
    else:
        print(currentNum,'is prime.')