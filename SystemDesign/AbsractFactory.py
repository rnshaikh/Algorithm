"""
Abstract Factory Method is a Creational Design pattern that allows
you to produce the families of related objects without specifying their concrete classes
"""

class AbstractFactory:
    
    def __init__(self, factory):
        self.factory = factory
        
    def show_course(self):
        obj = self.factory()
        print(f"Course name {obj}")
        print(f"Fee {obj.fee()}")
    

class DSA:
    
    def __str__(self):
        return "DSA"
        
    def fee(self):
        return 800
        
class STL:
    
    def __str__(self):
        return "STL"
    
    def fee(self):
        return 1000
        
class Algorithm:
    
    def __str__(self):
        return "Algorithm"
        
    def fee(self):
        return 

        

obj = AbstractFactory(STL)
obj.show_course()

