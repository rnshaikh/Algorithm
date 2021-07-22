


#Function to reverse first k elements of a queue.


"""
    1) take stack and list
    2) push k element from q into stack
    3) append remaining element to list
    4) enqueue element from stack first .
    5) enqueue element from list then
    6) return q

"""




def modifyQueue(q,k):
    # code here


    stack = []
    lis = []
    while k>0:
        ele = q.pop(0)
        stack.append(ele)
        k = k-1

    while len(q):
        lis.append(q.pop(0))

    while(len(stack)):
        ele = stack.pop(-1)
        q.append(ele)

    while(len(lis)):
        q.append(lis.pop(0))

    return q
