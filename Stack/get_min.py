#Get minimum element from stack

"""
    Push(x) : Inserts x at the top of stack.
            If stack is empty, insert x into the stack and make minEle equal to x.
            If stack is not empty, compare x with minEle. Two cases arise:
            If x is greater than or equal to minEle, simply insert x.
            If x is less than minEle, insert (2*x – minEle) into the stack and make minEle equal to x. For example, let previous minEle was 3. Now we want to insert 2. We update minEle as 2 and insert 2*2 – 3 = 1 into the stack.

    Pop() : Removes an element from top of stack.
        Remove element from top. Let the removed element be y. Two cases arise:
        If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
        If y is less than minEle, the minimum element now becomes (2*minEle – y), so update (minEle = 2*minEle – y). This is where we retrieve previous minimum from current minimum and its value in stack. For example, let the element to be removed be 1 and minEle be 2. We remove 1 and update minEle as 2*2 – 1 = 3.

"""

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if self.minEle is None:
            self.minEle = x
            self.s.append(x)
            return

        else:
            if self.minEle>x:

                ele = ((2*x) - self.minEle)
                self.minEle = x
                self.s.append(ele)
                return
            else:
                self.s.append(x)



    def pop(self):
        #CODE HERE

        if len(self.s)<=0:
            self.minEle = None
            return -1

        ele = self.s.pop()
        if ele>=self.minEle:
            if len(self.s)<=0:
                self.minEle = None
            return ele

        else:
            removed = self.minEle
            newMin = ((2*self.minEle) - ele)
            self.minEle = newMin
            return removed


    def getMin(self):
        #CODE HERE
        if len(self.s)<=0:
            return -1

        return self.minEle
