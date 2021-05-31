# Count Pairs whose sum is equal to X

"""
Method1:
    1) intiates temp1, temp2 and count=0 and set lis
    2) traverse first list save in set list
    3) traverse second list and check if x - list2.data in set if yes increment count
    4) return count

"""

class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        '''
        h1:  head of linkedList 1
        h2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:   len of linkedList 1
        X:   given sum
        '''
        temp1 = h1
        temp2 = h2
        count = 0
        lis = set()

        while temp1 != None:
            lis.add(temp1.data)
            temp1 = temp1.next

        while(temp2 != None):
            sub = x-temp2.data
            if sub in lis:
                count = count+1
            temp2 = temp2.next

        return count
