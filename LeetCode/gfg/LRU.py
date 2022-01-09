
"""
    using hash map and doubly linked list with 0 at front and last node
    O(1) for get and set

"""



#User function Template for python3

# design the class in the most optimal way
class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = None
        self.prev = None



class LRUCache:

    #Constructor for initializing the cache capacity with the given value.
    def __init__(self,cap):
        #code here

        self.hash_map = {}
        self.cap = cap
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):

        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node


    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.hash_map:
            key_node = self.hash_map[key]
            self.remove(key_node)
            self.insert(key_node)
            return key_node.value
        else:
            return -1


    #Function for storing key-value pair.
    def set(self, key, value):
        #code here
        if key in self.hash_map:
            key_node = self.hash_map[key]
            self.remove(key_node)
            del self.hash_map[key]

        node = Node(key, value)
        self.insert(node)
        self.hash_map[key] = node

        if len(self.hash_map) > self.cap:
            left_node = self.left.next
            self.remove(left_node)
            del self.hash_map[left_node.key]
