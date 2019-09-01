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
 
#Operator overloading
"""
Ex: 
    
5+6 == int.__add__(5,6)
Here 5 and 6 are the integer operands and + is operator, in the same way we can do addition of integers, floats, strings 
what if you want to do 5 + 'Hello World' - it will give you an error of unsupported operand types, because there is no inbuilt method to add integers and strings
so all this kind of methods (int.__add__(), str.__add__()) are predefined, it is called as Synthetic Sugar
"""

class Student:
    
    def __init__ (self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    # method for add operator overloading 
    def __add__ (self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student (m1, m2)
        return s3
    
        
s1 = Student (56,78)
s2 = Student (34,98)

"""
if you want to add that two students marks 
Ex: s3 = s1 + s2
it will give you an error of unsupported operand types, beause there is no add method in the Student calss
but it is possible to define the method, which is called operator overloading 
"""
# Now it is possible to add , in the same way you can define other method like multiplication, greater, substraction, etc
s3 = s1 +s2
print (s3.m1)
print (s3.m2)
