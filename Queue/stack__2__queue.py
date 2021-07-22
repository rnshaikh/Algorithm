#Stack using two queues

"""
    1) at time of insert insert ele at o pos by removing all ele to 2nd queue and after adding current again add all element from 2nd queue
    2) at time of pop pop element from first position

"""



def push(x):

    # global declaration
    global queue_1
    global queue_2

    # code here
    if not len(queue_1):
        queue_1.append(x)
        return

    while len(queue_1):
        ele = queue_1.pop(0)
        queue_2.append(ele)

    queue_1.append(x)
    while len(queue_2):
        ele = queue_2.pop(0)
        queue_1.append(ele)

#Function to pop an element from stack using two queues.
def pop():

    # global declaration
    global queue_1
    global queue_2

    # code here
    if not len(queue_1):
        return -1

    ele = queue_1.pop(0)
    return ele
