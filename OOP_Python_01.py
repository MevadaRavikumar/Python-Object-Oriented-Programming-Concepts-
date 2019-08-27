# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:09:48 2019

@author: Ravi
"""


"""
Types of Methods
1. Instance Method - works with instance and instacne variables
2. Class Method - works with class variables
                
        @classmethod 
        def classname (cls):  
            cls.class attribuits
            
3. Static Method - method which has nothing to do with instance or class variables, useful if you want to perform some 
                    operation which has to do something with other class object
         
"""
class Student:
    
    University = 'Ernst Abbe Hochschule'
    
    def __init__ (self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method: because it depends on object or instance
    def avg (self):
        return (self.m1+self.m2+self.m3)/3
    # accessors method (getters)
    def get_m1 (self):
        return self.m1
    # mutatores method (setters)
    def set_m1 (self, value):
        self.m1 = value
  
    # class method
    @classmethod
    def getschoolname (cls):
        return cls.University
    @staticmethod    
    def info ():
        print ("This is static method!")
        
s1 = Student(60, 70, 78)
s2 = Student(90, 92, 65)

print (s1.avg())
print (s2.avg())
print (s1.getschoolname())
print (Student.getschoolname())
print (Student.info())