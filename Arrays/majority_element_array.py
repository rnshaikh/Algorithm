
# Find majority element in Array : element whoc occure more than N/2 times
"""
    Method :
        1) get hash_count {}
        2) traverse array if its not in hash add element as key value 1 else increment count by 1 of given element
        3) get list of hash_count value and hash_count keys find out maximum value key
        4) if all value is same and no of element grater than 1 then return -1
        5) if count > N/2 return that element
        6) else return -1
"""

class Solution:
    def majorityElement(self, A, N):

        #Your code here

        hash_count = {}
        present = N/2

        for i in range(0,len(A)):

            if A[i] in hash_count:
                count = hash_count[A[i]] + 1
                hash_count[A[i]] = count
            else:
                hash_count[A[i]] = 1

        v=list(hash_count.values())
        k=list(hash_count.keys())
        element=k[v.index(max(v))]
        max_count = max(v)

        res = len(list(set(list(hash_count.values())))) == 1

        if res and N>1:
            return -1

        if element and max_count>present:
            return element

        else:
            return -1




















