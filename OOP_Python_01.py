# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:09:48 2019

@author: Ravi
"""


"""
Things which will cover in inheritance
1. Single level inheritance
2. Multi level inheritance
3. Multipal inheritance
4. Constructor in inheritance
"""

# Here class A is super class
class A:
    def method1(self):
        print ("This is method 1")
    def method2(self):
        print ("This is method 2")

# Here class B is sub class 
# To inherit class A you just need to mention that class name during the defination of class B in ()
        
class B(A):
    def method3(self):
        print ("This is method 3")
    def method4(self):
        print ("This is method 4")
        
# Here class A is only having method 1&2 because class A is not inheriting class B
a = A()
a.method1()
a.method2()

# Here class B is having class A's methods as well as its own methods 
# This is called single level of inheritance
b = B()
b.method1()
b.method2()
b.method3()
b.method4()