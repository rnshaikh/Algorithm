

class Obj:
    
    def __init__(self, val):
        self.val = val
    
    
    def __add__(self, obj2):
        return self.val + obj2.val
        
    def __sub__(self, obj2):
        return self.val - obj2.val
    
    def __mul__(self, obj2):
        return self.val * obj2.val
        
    def __floordiv__(self, obj2):
        return self.val // obj2.val
        
    def __mod__(self, obj2):
        return  self.val % obj2.val

    def __truediv__(self, obj2):
        return self.a / obj2.a 


a = Obj(5)
b = Obj(7)
print(a+b)
print(a-b)
print(a*b)
print(a//b)


def sum(a, b, *args):
    
    res= a+b
    for i in args:
        res += res
    return res
    


print(sum(7, 5))
print(sum(7,5,10,11,12))
print(sum(7.0, 5.4, 11.456))
