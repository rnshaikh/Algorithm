class Solution:
    # your task is to complete this function
    # function should print the top view of the binary tree
    # Note: You aren't required to print a new line after every test case
    
    
    def find(self, root, curr_length, prev_data, res):
        
        if not root:
            return
        
        if root.data == prev_data:
            curr_length = curr_length+1
        else:
            curr_length = 1
            
        res[0] = max(res[0], curr_length)
        
        self.find(root.left, curr_length, root.data+1, res)
        self.find(root.right, curr_length, root.data+1, res)
        
        
    def longestConsecutive(self, root):
        # Code here
        
        res = [0]
        
        self.find(root, 0, root.data, res)
        
        if res[0] == 1:
            return -1
            
        return res[0]
