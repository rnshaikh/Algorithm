"""
A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.


"""
# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))







from abc import ABC, abstractmethod

class A(ABC):
    
    @abstractmethod
    def abs_method(self):
        pass
    
    def nor(self):
        print("Normal")
        

class B(A):
    
    def abs_method(self):
        print("Abstrct method", self)
    
    @classmethod
    def cl_method(cls):
        print("class method", cls)
        
    @staticmethod
    def st():
        print("Static method")
        
        

b = B()
b.nor()
b.abs_method()
b.st()
B.cl_method()