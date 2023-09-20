from heapq import heappush, heapify
import time


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.root = None
        self.start = ListNode(-1)
        self.end = ListNode(-1)
        self.start.next = self.end
        self.end.prev = self.start

    def insert(self, node):
        previous = self.end.prev
        previous.next = node
        node.prev = previous
        node.next = self.end
        self.end.prev = node
    
    def remove(self, node):
        previous = node.prev
        nex = node.next
        
        previous.next = nex
        nex.prev = previous


class BinarySearch:
    def __init__(self):
        self.root = None

    def get_min(self):
        temp = self.root
        while temp and temp.left:
            temp = temp.left
        return temp
    
    def get_min_by_root(self, root):
        
        temp = root
        while temp and temp.left:
            temp = temp.left
        return temp


class ExpiryNode:
    def __init__(self, time):
        self.expiry_time = time
        self.keys = set()
        self.left = None
        self.right = None
        
    def delete_any_key(self):
        
        key = self.keys.pop()
        if not key:
            pass
        return key
    
    def delete_key(self, key):
        self.keys.remove(key)
        if not self.keys:
            pass
        

class PriorityNode:
    def __init__(self, pri):
        self.pri = pri
        self.list = DLL()
        self.lru = {}
        self.left = None
        self.right = None
        
    def delete_key(self, key):
        node = self.lru[key]
        self.list.remove(node)
        del self.lru[key]
        

class ExBinarySearch(BinarySearch):
    def __init__(self):
        super().__init__()
        
    def get_node(self, exp_time):
        temp = self.root
        while temp:
            if temp.expiry_time > exp_time:
                temp = temp.left
            elif temp.expiry_time < exp_time:
                temp = temp.right
            else:
                return temp
        return None
        
    def insert_node(self, node):
        temp = self.root
        prev = temp
        
        if not temp:
            self.root = node
            return
            
        while temp:
            if temp.expiry_time > node.expiry_time:
                prev = temp
                temp = temp.left
            elif temp.expiry_time < node.expiry_time:
                prev = temp
                temp = temp.right
        
        if prev.expiry_time > node.expiry_time:
            prev.left = node
        else:
            prev.right = node
            
    def delete_node(self, root, node):
        if root == None:
            return root

        elif root.expiry_time>node.expiry_time :
            root.left = self.delete_node(root.left, node)

        elif root.expiry_time<node.expiry_time:
            root.right = self.delete_node(root.right, node)

        else:
            if(root.left == None and root.right==None):
                del root
                root = None

            elif(root.left == None):
                temp = root
                root = root.right
                del temp

            elif(root.right == None):
                temp = root
                root = root.left
                del temp
            else:
                minnode = self.get_min_by_root(root.right)
                root.expiry_time = minnode.expiry_time
                root.right = self.delete_node(root.right, minnode)
        return root
    
    def print_tree(self):
        
        queue = []
        queue.append(self.root)

        while len(queue):
            node = queue.pop(0)
            print("node present: expiry_time, keys ", node.expiry_time, node.keys)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
            
    
class PriBinarySearch(BinarySearch):
    def __init__(self):
        super().__init__()
        
    def get_node(self, pri):
        temp = self.root
        while temp:
            if temp.pri > pri:
                temp = temp.left
            elif temp.pri < pri:
                temp = temp.right
            else:
                return temp
        return None
        
    def insert_node(self, node):
        temp = self.root
        prev = temp
        
        if not temp:
            self.root = node
            return
            
        while temp:
            if temp.pri > node.pri:
                prev = temp
                temp = temp.left
            elif temp.pri < node.pri:
                prev = temp
                temp = temp.right
        
        if prev.pri > node.pri:
            prev.left = node
        else:
            prev.right = node
    
    def delete_node(self, root, node):
        if root == None:
            return root

        elif root.pri>node.pri :
            root.left = self.delete_node(root.left, node)

        elif root.pri<node.pri:
            root.right = self.delete_node(root.right, node)

        else:
            if(root.left == None and root.right==None):
                del root
                root = None

            elif(root.left == None):
                temp = root
                root = root.right
                del temp

            elif(root.right == None):
                temp = root
                root = root.left
                del temp
            else:
                minnode = self.get_min_by_root(root.right)
                root.pri = minnode.pri
                root.right = self.delete_node(root.right, minnode)
        return root
    
    def print_tree(self):
        
        queue = []
        queue.append(self.root)

        while len(queue):
            node = queue.pop(0)
            print("node present: priority tree ", node.pri, node.lru)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
            
    
class PECache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        self.expiry_tree = ExBinarySearch()
        self.priority_tree = PriBinarySearch()
        
    def remove_set(self, key, pri, expiry):
        
        expiry_node = self.expiry_tree.get_node(expiry)
        expriry_node.delete_key(key)
        
        pri_node = self.priority_tree.get_node(pri)
        pri_node.delete_key(key)
    
    
    def insert_pri(self, key, pri):
        pri_node = self.priority_tree.get_node(pri)
        if pri_node:
            if key in pri_node.lru:
                list_node = pri_node.lru[key]
                list_node.list.delete(list_node)
                list_node.list.insert(list_node)
            else:
                list_node = ListNode(key)
                pri_node.list.insert(list_node)
                pri_node.lru[key] = list_node
                
        else:
            pri_node = PriorityNode(pri)
            list_node = ListNode(key)
            pri_node.list.insert(list_node)
            self.priority_tree.insert_node(pri_node)
            pri_node.lru[key] = list_node
                
    
    def insert_set(self,key, pri, expiry):
        
        expiry_node = self.expiry_tree.get_node(expiry)
        if expiry_node:
            if key in expiry_node.keys:
                self.insert_pri(key, pri)
                return
            expiry_node.keys.add(key)
            self.insert_pri(key, pri)
        else:
            expiry_node = ExpiryNode(expiry)
            expiry_node.keys.add(key)
            self.expiry_tree.insert_node(expiry_node)
            self.insert_pri(key, pri)
    
    def evict_item(self):
        curr_time = int(time.time())
        expiry_min_node = self.expiry_tree.get_min()
        if expiry_min_node.expiry_time < curr_time:
            key_to_delete = expiry_min_node.delete_any_key()
            pri_to_delete = self.cache[key_to_delete][2]
            pri_node = self.priority_tree.get_node(pri_to_delete)
            pri_node.delete_key(key_to_delete)
            del self.cache[key_to_delete]
            if not pri_node.lru:
                self.priority_tree.delete_node(self.priority_tree.root, pri_node)
            if not expiry_min_node.keys:
                self.expiry_tree.delete_node(self.expiry_tree.root, expiry_min_node)
                
            
        else:
            pri_min_node = self.priority_tree.get_min()
            delete_list_node = pri_min_node.list.start.next
            key_to_delete = delete_list_node.key
            pri_min_node.delete_key(key_to_delete)
            
            expiry_to_delete = self.cache[key_to_delete][1]
            expiry_node = self.expiry_tree.get_node(expiry_to_delete)
            expiry_node.delete_key(key_to_delete)
            del self.cache[key_to_delete]
            if not pri_min_node.lru:
                #print("deleting prioruty node", pri_min_node.pri)
                #print("ater deleting ", self.priority_tree.print_tree())
                self.priority_tree.delete_node(self.priority_tree.root, pri_min_node)
            if not expiry_node.keys:
                self.expiry_tree.delete_node(self.expiry_tree.root, expiry_node)
                
        # self.expiry_tree.print_tree()
        # self.priority_tree.print_tree()
        
            
    def evict_items(self):
        
        if len(self.cache) > self.cap:
            self.evict_item()
            
    def set(self, key, value, pri, expiry):
    
        curr_time = time.time()
        curr_time += expiry
        curr_time = int(curr_time)
        
        if key in self.cache:
            key, expiry_time, pri = self.cache[key]
            self.remove_set(key, expiry_time, pri)
            
        self.cache[key] = (value, curr_time, pri)
        self.insert_set(key, pri, curr_time)
        self.evict_items()
        
    def get(self, key):
        self.evict_items()
        if key not in self.cache:
            return -1

        pri_node = self.priority_tree.get_node(self.cache[key][2])
        list_node = pri_node.lru[key]
        pri_node.list.remove(list_node)
        pri_node.list.insert(list_node)
        return self.cache[key][0]



obj = PECache(2)
print(obj.set(1, 1, 20, 0))
print(obj.set(2, 2, 10, 10))
print(obj.get(1))
print(obj.set(3, 3, 20, 10))
print(obj.get(2))
print(obj.set(4, 4, 30, 10))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
print(obj.get(2))
























import time


class ListNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DLL:
    
    def __init__(self):
        
        self.start = ListNode(-1)
        self.end = ListNode(-1)
        self.start.next, self.end.prev = self.end, self.start
    
    def insert(self, node):
        
        prev = self.end.prev
        
        prev.next = node
        node.prev = prev
        node.next = self.end
        self.end.prev = node
        
    def delete(self, node):
        
        prev = node.prev
        nex = node.next
        
        prev.next = nex
        nex.prev = prev
        
class BST:
    
    def __init__(self):
        self.root = None
    
    def get_min(self, root):
        
        temp = root
        while temp and temp.left:
            temp = temp.left
        return temp
       
    def get_node(self, data):
        
        temp = self.root
        while temp:
            if temp.data > data:
                temp = temp.left
            elif temp.data < data:
                temp = temp.right
            else:
                return temp
                
    def insert_node(self, node):
        
        prev = self.root
        temp = self.root
        
        if not self.root:
            self.root = node
            return
        
        while temp:
            
            if temp.data > node.data:
                prev = temp
                temp = temp.left
            elif temp.data < node.data:
                prev = temp
                temp = temp.right
                
        if prev.data > node.data:
            prev.left = node
        else:
            prev.right = node
    
    def delete_node(self, root, node):
        
        if not root:
            return
        
        if root.data > node.data:
            root.left = self.delete_node(root.left, node)
        elif root.data < node.data:
            root.right = self.delete_node(root.right, node)
        else:
            if not root.left and not root.right:
                del root
                return
            elif not root.left and root.right:
                temp = root
                root = root.right
                del temp
            elif root.left and not root.right:
                temp = root
                root = root.left
                del temp
            else:
                min_node = self.get_min(root.right)
                root.data = min_node.data
                root.right = self.delete_node(root.right, min_node)
                
class ExpiryNode:
    def __init__(self, expiry):
        self.data = expiry
        self.keys = set()
        self.left = None
        self.right = None
    
    def delete_any_key(self):
        if not self.keys:
            return 
        key = self.keys.pop()
        return key
        
    def delete_key(self, key):
        self.keys.remove(key)
        
        
class PriorityNode:
    
    def __init__(self, pri):
        self.data = pri
        self.lru = {}
        self.list = DLL()
        self.left = None
        self.right = None
    
    def delete_key(self, key):
        
        list_node = self.lru[key]
        self.list.delete(list_node)
        del self.lru[key]
        
class PECache:
    
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        self.priority_tree = BST()
        self.expiry_tree = BST()
        
        
    def expiry_cleanup(self, expiry, key):
        
        exp_node = self.expiry_tree.get_node(expiry)
        if exp_node:
            exp_node.delete_key(key)
        
    def priority_cleanup(self, pri, key):
        
        pri_node = self.priority_tree.get_node(pri)
        
        if pri_node:
            list_node = pri_node.lru[key]
            pri_node.list.delete(list_node)
            del pri_node.lru[key]
        
    def expiry_insert(self, expiry, key):
        
        exp_node = self.expiry_tree.get_node(expiry)
        
        if exp_node:
            if key not in exp_node.keys:
                exp_node.keys.add(key)
        
        else:
            exp_node = ExpiryNode(expiry)
            exp_node.keys.add(key)
            self.expiry_tree.insert_node(exp_node)
    
    def priority_insert(self, pri, key):
        
        pri_node = self.priority_tree.get_node(pri)
        if pri_node:
            if key in pri_node.lru:
                list_node = pri_node.lru[key]
                pri_node.list.delete(list_node)
                pri_node.list.insert(list_node)
            else:
                list_node = ListNode(key)
                pri_node.list.insert(list_node)
                pri_node.lru[key] = list_node
                
        else:
            pri_node = PriorityNode(pri)
            list_node = ListNode(key)
            pri_node.list.insert(list_node)
            pri_node.lru[key] = list_node
            self.priority_tree.insert_node(pri_node)
            
    
    def evict_item(self):
        
        exp_node = self.expiry_tree.get_min(self.expiry_tree.root)
        curr_time = int(time.time())
        
        if exp_node.data < curr_time:
            
            key_to_delete = exp_node.delete_any_key()
            pri_to_delete = self.cache[key_to_delete][1]
            
            pri_node = self.priority_tree.get_node(pri_to_delete)
            list_node = pri_node.lru[key_to_delete]
            pri_node.delete_key(key_to_delete)
            del self.cache[key_to_delete]
            del pri_node.lru[key_to_delete]
            
            
            if not pri_node.lru:
                self.priority_tree.delete(self.priority_tree.root, pri_node)
            
            if not exp_node.keys:
                self.expiry_tree.delete(self.expiry_tree.root, exp_node)
        else:
            pri_node = self.priority_tree.get_min(self.priority_tree.root)
            list_node = pri_node.list.start.next
            key_to_delete = list_node.key
            exp = self.cache[key_to_delete][2]
            exp_node = self.expiry_tree.get_node(exp)
            
            pri_node.delete_key(key_to_delete)
            exp_node.delete_key(key_to_delete)
            del self.cache[key_to_delete]
            
            if not pri_node.lru:
                self.priority_tree.delete_node(self.priority_tree.root, pri_node)
            
            if not exp_node.keys:
                self.expiry_tree.delete_node(self.expiry_tree.root, exp_node)
                
    def evict_items(self):
        
        if len(self.cache) > self.cap:
            self.evict_item()
            
        
    def set(self, key, value, pri, expiry):
        
        if key in self.cache:
            self.expiry_cleanup(self.cache[key][2], key)
            self.priority_cleanup(self.cache[key][1], key)
        
        curr_time = int(time.time())
        curr_time += expiry
        
        self.expiry_insert(curr_time, key)
        self.priority_insert(pri, key)
        self.cache[key] = (value, pri, curr_time)
        self.evict_items()
    
    def get(self, key):
        
        if key not in self.cache:
            return -1
        
        self.evict_items()
        
        if key not in self.cache:
            return -1
        
        value, pri, expiry = self.cache[key]
        pri_node = self.priority_tree.get_node(pri)
        list_node = pri_node.lru[key]
        pri_node.list.delete(list_node)
        pri_node.list.insert(list_node)
        return value
        
        
obj = PECache(2)
print(obj.set(1, 1, 20, 0))
print(obj.set(2, 2, 10, 10))
print(obj.get(1))
print(obj.set(3, 3, 20, 10))
print(obj.get(2))
print(obj.set(4, 4, 30, 10))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
print(obj.get(2))


            
    
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
                
                
                
            
        
        
        
        
        
        
                
                
                
                
                
                
                
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        