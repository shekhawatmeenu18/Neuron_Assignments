# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:18:36 2020

@author: 91997
"""

##Answer 1 ##
# Numbers btw 2000 and 3200, which are divisible by 7 but are not multiple of 5

req_number=[]
notreq_number=[]

for number in range (2000,3200):
    if(number%7==0 and number%5!=0):
        #print("{} is divisibe by 7 but not multiple of 5".format(number))
        req_number.append(number)
    else:
        #print("{} is not divisibe by 7 but a multiple of 5".format(number))
        notreq_number.append(number)

print("List of numbers divisibe by 7 but not multiple of 5:",req_number)

## Answer 2##
first=input("Enter first name: ")
last=input("Enter last name: ")
print(last+" " + first)


## Answer 3 ##
from math import pi

#def SphereVol(radius):
#    V= (4/3 * pi * (int(radius)^3))
#    return print("Vol of Sphere is:",V)
#SphereVol(6)

diameter=12
#radius=int(diameter/2)
V= (4/3 * pi * (int((diameter/2))^3))
print("Vol of Sphere is:",V)

