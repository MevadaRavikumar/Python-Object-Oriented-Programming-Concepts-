# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:09:48 2019

@author: Ravi
"""


"""
Types of Methods and Polymorphism

*Types of Methods
1. Instance Method - works with instance and instacne variables
2. Class Method - works with class variables
                
        @classmethod 
        def classname (cls):  
            cls.class attribuits
            
3. Static Method - method which has nothing to do with instance or class variables, useful if you want to perform some 
                    operation which has to do something with other class object
         
*Polymorphism
- Ploymorphism means many forms, here objects can have multiple form 
- four ways of implimenting polymorphism 
1. Duck Typing
2. Operator Overloading 
3. Method Overloading
4. Method Overriding
"""
class Student:
    
    University = 'Ernst Abbe Hochschule'
    
    def __init__ (self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop()  #object of Laptop class

    # instance method: because it depends on object or instance
    def avg (self):
        return (self.m1+self.m2+self.m3)/3
    # accessors method (getters)
    def get_m1 (self):
        return self.m1
    # mutatores method (setters)
    def set_m1 (self, value):
        self.m1 = value 
    def show (self):
        print (self.m1, self.m2, self.m3)

    # class method
    @classmethod
    def getschoolname (cls):
        return cls.University
    @staticmethod    
    def info ():
        print ("This is static method!")
    
    class Laptop: 
         def __init__(self):
             self.brand = 'Acer'
             self.cpu = 'i5'
             self.ram = '8GB'
         def show (self):
              print (self.brand, self.cpu, self.ram)
        
s1 = Student(60, 70, 78)
s2 = Student(90, 92, 65)

# creating object of lap
lap1 = s1.lap
lap2 = s2.lap

lap3 = Student.Laptop()

print (s1.avg())
print (s2.avg())
print (s1.getschoolname())
print (Student.getschoolname())
print (Student.info())
print (s1.lap.brand)
print (s2.lap.cpu)
print (lap1.cpu)
print (lap2.cpu)
print (lap3.show())
print (s1.show())

# Duck Typing 
# Duck typing is used when you have same kind og method in different classes and you want to call that method from those classes depending on the situation 
# There are two classes called acer and lenovo and both are having the same features method
class acer:
    def features(self):
        print ("i5 processor")
        print ("8GB RAM")
        print ("1TB HD")

class lenovo: 
    def features(self):
        print ("i7 processor")
        print ("16GB RAM")
        print ("512GB SSD HD")

class Laptop:  
    def show_feature (self, company):
        company.features() 

# Here the type of company object can be change from lenovo to acer or vise versa
# This is called duck typing 
company = lenovo()

lap1 = Laptop()
lap1.show_feature(company)
 