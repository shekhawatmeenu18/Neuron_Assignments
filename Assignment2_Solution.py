# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:19:20 2020

@author: 91997
"""

## Draw a pattern ##
def pattern(n):
    for num in range(n):
        for i in range(num):
            print("*",end=' ')
        print("")
    
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=' ')
        print("\r")

pattern(10)

## Answer 2 ##
word=input("Enter a Word: ")
print("Reverse Word:",word[::-1])