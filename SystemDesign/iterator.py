class It:

    def __iter__(self):
        self.val = 0
        return self

    def __next__(self):
        if self.val <= 100:
            temp = self.val
            self.val = self.val+1
            return temp
        else:
            raise StopIteration


inr = It()
ite_obj = iter(inr)

for i in ite_obj:
    print(i)




"""
    Generator

"""

def gen(n):

    for i in range(0, n+1):
        yield i


"""

Comparison between iterators and generators
In iterators, we need to make use of the interator protocol methods (iter() and next()) but generators are simpler as we only need to use a function.

Generators use yield, iterators don't.

Implementing our own iterators requires us writing a class as shown earlier, generators don't need classes in python.

Generators are faster than iterators but iterators are more memory-effecient.


"""

