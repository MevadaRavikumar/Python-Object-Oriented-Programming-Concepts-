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

# Class C is sub sub class
# Here class C is inheriting class B and class B is inheriting class A 

class C(B):
    def method5(self):
        print ("This is method 5")
    def method6(self):
        print ("This is method 6")
        
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

# class C will have all the methods of Class A and B and also its own
# This is called multi level of inheritance
c = C()
c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
c.method6()