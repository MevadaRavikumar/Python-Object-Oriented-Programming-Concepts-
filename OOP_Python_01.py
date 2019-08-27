# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:09:48 2019

@author: Ravi
"""


"""
Defining a class in Python

class <class name>:
    Here comes attribuit list and method            
"""



class Computer: 
    """
    Defined Computer class which is having config method to print configuration of objects.
    """    
    def config (self):
        print ("i5, 16gb, 1Tb")

# defined object(instance) of class Computer
# computer1 is an object(instance) of computer
computer1 = Computer()  

# you can know the type of the object 
print (type (computer1))

# calling the method of the class
#class name. method name(object name) 
Computer.config(computer1)
#or
# object name.method()  [Normally this convention is used]
computer1.config()
