# two stacks in single array

"""
    top1 should be increment when appending element by stack1
    top2 should be decrement when appending element by stack2


    pop:
        if top1 == -1  return -1
        remove ele a[top1]
        decrement top1 = top1-1
    pop2:
        if top2 == 101 return -1
        remove element a[top2]
        increment  top2 = top2+1
        return ele

"""



top1 = -1
top2 = 101

#Function to push an integer into the stack1.
def push1(a,x):
    #code here

    top1 = top1+1

    a[top1] = x


#Function to push an integer into the stack2.
def push2(a,x):
    #code here
    top2 = top2-1
    a[top2] = x


#Function to remove an element from top of the stack1.
def pop1(a):
    #code here
    if top1 == -1:
        return -1

    ele = a[top1]
    top1 = top1-1
    return ele


#Function to remove an element from top of the stack2.
def pop2(a):
    #code here
    if top2 == 101:
        return -1

    ele = a[top2]
    top2 = top2+1
    return ele
