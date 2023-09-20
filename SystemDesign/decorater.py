"""
Definition:

The decorator pattern attaches additional responsibilities to an object dynamically. 
Decorators provide a flexible alternative to subclassing for extending functionality.

decorator is wrapper function or object that provide additional functionality or feature to exist function or object at runtime

Each component can be used on its own or may be wrapped by a decorator.
Each decorator has an instance variable that holds the reference to component it decorates(HAS-A relationship).
The ConcreteComponent is the object we are going to dynamically decorate.

Advantages:

The decorator pattern can be used to make it possible to extend (decorate) the functionality of a certain object at runtime.
The decorator pattern is an alternative to subclassing. Subclassing adds behavior at compile time, 
and the change affects all instances of the original class; decorating can provide new behavior at runtime for individual objects.
Decorator offers a pay-as-you-go approach to adding responsibilities. Instead of trying to support all foreseeable 
features in a complex, customizable class, you can define a simple class and add functionality incrementally with Decorator objects.


Disadvantages:

Decorators can complicate the process of instantiating the component because you not only have to 
instantiate the component, but wrap it in a number of decorators.
It can be complicated to have decorators keep track of other decorators, 
because to look back into multiple layers of the decorator chain starts to push 
the decorator pattern beyond its true intent.

"""




class TextTool:

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

class UnderlineWrapper(TextTool):


    def __init__(self, obj):
        self._wrapper = obj


    def render(self):
        return "<u>{}</u>".format(self._wrapper.render())


class ItalicWrapper(TextTool):

    def __init__(self, obj):
        self._wrapper = obj

    def render(self):
        return "<i>{}</i>".format(self._wrapper.render())


class BoldWrapper(TextTool):

    def __init__(self, obj):
        self._wrapper = obj

    def render(self):
        return "<b>{}</b>".format(self._wrapper.render())



if __name__ == "__main__":


    before = TextTool("before_text")
    after  = BoldWrapper(ItalicWrapper(UnderlineWrapper(before)))

    print("Before", before.render())
    print("after", after.render())



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)





def decorator(flag):
    def parametrize(fun):
        def wrapper(name):
            
            print("doe", flag)
            fun(name)
        return wrapper
    return parametrize


@decorator(False)
def hello(name):
    print("hello "+ name)
    
hello("abc")




class Decorator:
    
    def __init__(self, fun, flag):
        self.fun = fun
        self.flag = flag
        
    def __call__(self, name):
        
        print("doe")
        self.fun(name)


def dec(flag):
    def wrapper(fun):
        return Decorator(fun, flag)
    return wrapper

@dec(True)
def hello(name):
    print("hello " + name)
    
hello("abc")