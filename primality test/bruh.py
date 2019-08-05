# -*- coding: utf-8 -*-
"""
@author: samuel
"""

minNum = 2

print ("greetings! i will go through a range of natural numbers and declare their primality!")

    
maxNum = int(input("enter max pls: "))

for currentNum in range(minNum,maxNum+1): #go thru a list of ints
    
    #print(currentNum,'currently. ', end='') #debug current int
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