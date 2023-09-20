"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. 
Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks 
(the same letter in the array), that is that there must be at least n units of time between any two same tasks
Return the least number of units of times that the CPU will take to finish all the given tasks.

"""

"""
ALgorithm:

    it is pattern :
    maximum_row = maximum_freq_ele
    last_row_length = count(maximum_rows in values array)
    result = max((maximum_rows-1) * (n+1) + last_row_length, len(tasks))

"""



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        dic = {}

        if n == 0:
            return len(tasks)

        for i in tasks:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1

        values = dic.values()
        max_rows = max(values)

        last_row = 0
        for i in values:
            if i == max_rows:
                last_row = last_row + 1

        result = ((max_rows-1) * (n+1)) + last_row
        return max(result, len(tasks))










class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hash_map = {}
        max_count = 1
        
        if n == 0:
            return len(tasks)
        
        for i in tasks:
            if i in hash_map:
                hash_map[i] = hash_map[i] + 1
                max_count = max(max_count, hash_map[i])
            else:
                hash_map[i] = 1
                
                
        max_count_freq = 0
        
        for key, value in hash_map.items():
            if hash_map[key] == max_count:
                max_count_freq += 1
                
        
        print("max", max_count, max_count_freq) 
        result = ((max_count-1) * (n+1)) + max_count_freq
        
        return max(result, len(tasks))
                
                
            