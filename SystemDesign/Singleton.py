class A():
    
    def __new__(cls):        
        if hasattr(cls, 'instance'):
            return cls.instance
            
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("Initializing object")
    
    def hello(self):
        print("Hello world", self)
        


obj = A()
obj2 =A()

print(obj is obj2)
print(isinstance(obj, A))

obj.hello()
obj2.hello()



class Single:
    instance = None
    
    def __init__(self):
        if Single.instance:
            raise Exception("Cant instantiated Obj")
        
        Single.instance = self
        
    def hello(self):
        print("hell0", self.instance)
    
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance


obj2 = Single()
obj = Single.get_instance()
obj1 = Single.get_instance()
        
obj.hello()
obj1.hello()
obj2.hello()

