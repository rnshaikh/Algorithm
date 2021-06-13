# implement Queue using 2 stacks

#  in pushing push element in stack at the end so first element always on top
# deque remove element from top



#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''

    while len(stack1)>0:
        stack2.append(stack1[-1])
        stack1.pop()

    stack1.append(x)

    while len(stack2) > 0:
        stack1.append(stack2[-1])
        stack2.pop()




#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):

    '''
    stack1: list
    stack2: list
    '''
    #code here

    if len(stack1) <=0:
        return -1

    data = stack1[-1]
    stack1.pop()
    return data
