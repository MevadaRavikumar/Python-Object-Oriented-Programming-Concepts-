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
    * Defined Computer class which is having config method to print configuration of objects.
    * __init__ is a special method which initialize the variables, it it just like constructor in other languages like java, c++
    * The size of an object depends on no. of variables and soze of variables
    * __init__ method decides the allocation and size if the attribuits in the systems heap memory
    * self is a default parameter which takes instances as a value 
    """  
    def __init__ (self, CPU, RAM, HD):
        self.CPU = CPU
        self.RAM = RAM
        self.HD = HD
        
    def config (self):
        print ("CPU is ", self.CPU,"RAM is", self.RAM, "HD is", self.HD)

# defined object(instance) of class Computer
# computer1&2 is an object(instance) of computer
computer1 = Computer('i5', '8GB', '1TB')  
computer2 = Computer('i7', '16GB', '500 GB')  

# changing the values of any attribuit
# objects name.attribuits name which you want to alter = attribuits new value
computer1.CPU = 'i7'
computer2.RAM = '4GB'

# you can know the type of the object 
print (type (computer1))

# calling the method of the class
#class name. method name(object name) 
Computer.config(computer1)
#or
# object name.method()  [Normally this convention is used]
computer1.config()
computer2.config()
