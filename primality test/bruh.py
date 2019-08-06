# -*- coding: utf-8 -*-
"""
@author: samuel
"""

import math

def primalityOpti():

    print("greetings! i will go through a range of natural numbers and declare their primality!")
    
    minNum = 4
    maxNum = int(input("enter max pl0xXz!!!11: "))
    
    for currentNum in range(minNum,maxNum+1): #go thru a list of ints
        
        #print(currentNum,'currently. ', end='') #debug current int

        isPrime = bool(True)
        
        if currentNum % 2 == 0 or currentNum % 3 == 0: 
            isPrime = False
        else: #find if current int is a multiple of 6k+1
            for k in range(0,int(math.sqrt(currentNum))): 
                if currentNum % 6*k+1 == 0:
                    isPrime = False
                else:
                    isPrime = True       
                
        if isPrime is False:    #gives the pretty result.
            print(currentNum,'is composite.')
        elif isPrime is True:
           print(currentNum,'is prime.') 
           
# !!! testing below !!!
           
maxNum = int(input("enter max pls: "))

for currentNum in range(minNum,maxNum+1): #go thru a list of ints
    numFac = 0
    for potFac in range(minNum,currentNum): #seek potential factors
     
        #print ('testing if',potFac,'is a factor. ',end='') #debug current potential factor
            if currentNum % potFac == 0:
                #print (potFac, end=' is a factor. ')
                numFac += 1
                break       
    
    if numFac == 0:
     print(currentNum,'is prime.')
    else:
     print(currentNum,'is composite.')