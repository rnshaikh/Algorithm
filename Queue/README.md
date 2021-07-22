
# Queue

    Queue is linear data structure which perform the operation in FIFO
    element which added first is removed first

    Queue have two end front and rear
    front = used to remove element
    rear = used to add element

    enqueue = adding element
    dequeue = removing element

    isEmpty = checking if it is empty


# Application

    Queue is used when things don’t have to be processed immediatly, but have to be processed in First InFirst Out order like Breadth First Search. This property of Queue makes it also useful in following kind of scenarios.
    1) When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.
    2) When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes. Examples include IO Buffers, pipes, file IO, etc.


# implementation
    Queue is implement throuh array and linkedlist and stacks as well.




# Priority Queue

    Priority Queue is an extension of queue with following properties.

        Every item has a priority associated with it.
        An element with high priority is dequeued before an element with low priority.
        If two elements have the same priority, they are served according to their order in the queue.

    it has following operations:
        insert - insert element at the end
        getHighPriority - get high priority element
        deleteHighestPriority = delete high priority element


# implementation
    Array  and linkelist -- insert -- o(1), gethighpriority -- o(n), deletehighpriority--- o(n)
    Binary Heap, getHighestPriority() can be implemented in O(1) time, insert() can be implemented in O(Logn) time and deleteHighestPriority() can also be implemented in O(Logn) time.

    python moduleq have heap data structure.




# Dequeue

    Dequeue is double ended queue
    it support add and removing element from both end

    operations:

        insertFront(): Adds an item at the front of Deque.
        insertRear(): Adds an item at the rear of Deque.
        deleteFront(): Deletes an item from front of Deque.
        deleteRear(): Deletes an item from rear of Deque.


        getFront(): Gets the front item from queue.
        getRear(): Gets the last item from queue.
        isEmpty(): Checks whether Deque is empty or not.
        isFull(): Checks whether Deque is full or not.

# implementation:

    doubly linked list and circular array

    in python collections package have dequeue


