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
    def method_1 (self):
        print ("This is method1 in X")

#Sub class
        
class Y(): 
    def __init__ (self):
        #super().__init__()  # in this way you call call super class's init method
        print ("in Y init")
    def method3 (self):
        print ("This is method3")
    def method4 (self):
        print ("This is method4")
    def method_1 (self):
        print ("This is method1 in Y")

class Z(X,Y): 
    def __init__ (self):
        #super().__init__()  # in this way you call call super class's init method
        print ("in Y init")
    def method5 (self):
        print ("This is method3")

y = Y()
z = Z()
# here y will be having all the method from class X and Y
# When we run the code, it will print inti of class x since class Y is not having its own inti method
# When the class Y is having its own init method then init of class Y will be executed 
# When we call super().__init__() in class Y, both the init method will be executed
y.method1()

# Z is inheriting both X and Y class 
# when we call super method in Z then it will execute X's init method not Y's
#It will always give priority to the left side's super class then to right side (X,Y)
# This is called MRO Method Resolution Order (always from left to right)
# There same method called method_1 in class X and Y and class Z is inheriting both the class
z.method3()

# When we call this method_1 using z object then it will call class X's method_1, the same MRO goes to method also 
z.method_1()