from abc import ABC, abstractmethod
from tempfile import gettempprefix


class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        print("Abstract start")

    def stop(self):
        print("Abstract stop")


class Car(Vehicle):

    def __init__(self):
        self._wheel = 4
        self.__brakes = 5
    

    def get_breaks(self):
        print("Get called")
        return self.__brakes
    
    def set_breaks(self, value):
        print("Set called")
        self.__brakes = value

    def start(self):
        super().start()
        print("Car Started")

    def stop(self):
        super().stop()
        print("Car stopped")

    brakes = property(get_breaks, set_breaks)


if __name__ == "__main__":

    car = Car()
    car.start()
    car.stop()
    car.brakes = 10
    print(car.brakes)




from abc import ABC, abstractmethod

class Base(ABC):
    
    @abstractmethod
    def add(self, b):
        pass
    
    def sub(self, b):
        pass
    
    def mul(self, b):
        pass
    

class Derive(Base):
    
    
    def __init__(self, a):
        self.a = a
        
    def add(self, b):
        return self.a + b
    
    def sub(self, b):
        return self.a - b
        
    def mul(self, b):
        return self.a * b
        
    
obj = Derive(10)
print(obj.add(5))
print(obj.add(6))
print(obj.add(7))



class A:
    def __init__(self):
        self.a = 10
        
    def hello(self):
        print("Hello A")
        
        
class B:
    
    def __init__(self):
        self.a = 20
        
    def hello(self):
        print("Hello B")


class C(B, A):
    
    c = 10
    
    def __init__(self):
        self.__a = 10
    
    
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, a):
        self.__a = a
        
    @classmethod
    def inc(cls):
        print("print", cls)
        cls.c += 1
        print(cls.c)
    
    def world(self):
        print("World")
        

obj = C()
obj.hello()
print(obj.a)

C.inc()
obj.inc()

obj.a = 20
print(obj.a)
        
        
        
        
        
        
        
        
        
        
        

