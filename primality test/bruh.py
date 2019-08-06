# -*- coding: utf-8 -*-
"""
@author: samuel
"""

import math

print("greetings! i will go through a range of natural numbers and declare their primality!")

minNum = 4
maxNum = int(input("enter max pl0xXz!!!11: "))

for currentNum in range(minNum,maxNum+1): #go thru a list of ints
    
    #print(currentNum,'currently. ', end='') #debug current int
    numFac = 0
    isPrime = bool(True)
    
    if currentNum % 2 == 0 or currentNum % 3 == 0:
        isPrime = False
    else:
        for k in range(0,int(math.sqrt(currentNum))):
            if currentNum % 6*k+1 == 0:
                isPrime = False
            else:
                isPrime = True       
            
    if isPrime is False:
        print(currentNum,'is composite.')
    elif isPrime is True:
       print(currentNum,'is prime.') 
       
       