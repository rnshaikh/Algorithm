from monk import A

def hello(self):
    print("bye")

A.hello = hello

obj = A()

print(obj.hello())