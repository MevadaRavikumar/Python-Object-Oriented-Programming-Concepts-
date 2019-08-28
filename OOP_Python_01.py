# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:09:48 2019

@author: Ravi
"""


"""
Things which will cover in inheritance

1. Constructor in inheritance
2. MRO (Method Resolution Order)
"""
# Super class
class X: 
    def __init__ (self):
        print ("in X init")
    def method1 (self):
        print ("This is method1")
    def method2 (self):
        print ("This is method2")

#Sub class
        
class Y(X): 
    def __init__ (self):
        super().__init__()  # in this way you call call super class's init method
        print ("in Y init")
    def method3 (self):
        print ("This is method3")
    def method4 (self):
        print ("This is method4")


y = Y()

# here y will be having all the method from class X and Y
# When we run the code, it will print inti of class x since class Y is not having its own inti method
# When the class Y is having its own init method then init of class Y will be executed 
# When we call super().__init__() in class Y, both the init method will be executed
y.method1()
