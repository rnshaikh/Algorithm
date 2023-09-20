
"""
Monkey Patching in Python

Monkey Patching is an exciting topic of Python. Monkey-patching is a term that refers to modifying a class or module at a run time. 
In simple words, a class or module's work can be changed at the runtime. Let's understand this concept by real-life example.

When we work on a large project, we may encounter a situation where the third-party library is not working well. So we attempt to revise (or change) it from our project. This process is known as monkey patching in Python. Generally, it is avoided by the developer. However, it is a part of the development process.

In monkey patching, we can reopen the class and modify its behavior

We will learn how we can use monkey-patching in using the Python code.
Play Videox


We know that Python
is a dynamic language; classes are mutable, so we can alter them when we want. Let's understand the following example.


"""


"""
Example -
"""
import inspect  
  
  
class MonkeyPatch:  
    def __init__(self, n1):  
        self.n1 = n1  
  
    def add(self, other):  
        return (self.n1 + other)  
  
  
obj1 = MonkeyPatch(10)  
obj1.add(20)  
print(inspect.getmembers(obj1, predicate=inspect.ismethod))  


"""
Output:

30
[('__init__', >), ('add', >)]
As we can see in the above code, there are two methods in the above class - __init__ and addition. We called the add() method and passed 20 as an argument. It retuned 30. We have defined the MultiPatch class with the add() method. Suppose we add the new method to the MonkeyPatch class.

"""

def divide(self, n2):  
    return(self.n1 - self.n2)  

"""    
To add the divide() method to MonkeyPatch class, simply assign the divide function to MonkeyPatch.

"""

MonkeyPatch.divide = divide  

"""
Dynamic Behavior of Function
Let's see another example to understand the dynamic behavior in better way.

Example -
"""

# new_monk.py  
class A:  
   def hello(self):  
      print (" The hello() function is being called")  

"""
We have created a module which will use in the below code to change the behavior of hello() function at runtime.
"""
"""
import new_monk  

"""
def monkey_f(self):  
   print ("monkey_f() is being called")  

  
# replacing address of "func" with "monkey_f"  
new_monk.A.hello = monkey_f  
obj = new_monk.A()  
  
# calling function "func" whose address got replaced  
# with function "monkey_f()"  
obj.hello() 

"""
Output:
monkey_f() is being called

"""
