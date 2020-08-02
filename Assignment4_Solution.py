# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 00:49:34 2020

@author: 91997
"""
### Answer 1.1 ###
class triangleSides:
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3


class areaTriangle(triangleSides):
    def __init__(self,side1,side2,side3):
        super().__init__(side1,side2,side3)
        
    def tri_area(self):
        s=(self.side1+self.side2+self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
         

a1=areaTriangle(8,9,5)
print(a1.tri_area())
       
##Answer 2.1 ##
def filter_long_words(ele_count):        
    lst=[]
    #ele_count=int(input("Lenght of elements:" ))
    for elements in range(0,ele_count):
        ele=input("Enter a word: ")
        lst.append(ele)
    print("List of words:" ,lst)
    
    string_len=[]
    for element in lst:
        if (len(element)>=ele_count):
            string_len.append(element)
        else:
            pass
    return print("List of words lenght >={} :".format(ele_count) , string_len)


## Answer 2.1 ##
def len_list(n):
    lst=[]
    for i in range(0,n):
        ele=input("Enter a string:")
        lst.append(ele)
    print("List elements:",lst)
    
    string_len=[]
    
    for string in lst:
        string_len.append(len(string))
    print("Length of string elements:",string_len)
    
len_list(3)

## Answer 2.2 ##
def wovel_identify2():
    ele=input("Enter the alphabet:" )   
    while len(ele)>1:
        print("Can't accept as alphabet length is>1")
        ele=input("Re-Enter the alphabet:" )
    else:
        print("Entered correct alphabet!")

    lst=['a','e','i','o','u']
    if ele.lower() in lst:
        print('True')
    else:
        print('False')







