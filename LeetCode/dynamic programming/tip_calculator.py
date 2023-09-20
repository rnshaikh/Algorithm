"""

Rahul and Ankit are the only two waiters in the Royal Restaurant. Today, the restaurant received n orders.
The amount of tips may differ when handled by different waiters, if Rahul takes the ith order, he would be tipped ai rupees and if Ankit takes this order, the tip would be bi rupees.
In order to maximize the total tip value they decided to distribute the order among themselves. One order will be handled by
one person only. Also, due to time constraints Rahul cannot take more than x orders and Ankit cannot take more than y orders.
It is guaranteed that x + y is greater than or equal to n, which means that all the orders can be handled by either Rahul or Ankit.
Find out the maximum possible amount of total tip money after processing all the orders.

"""


"""
    greedy approach:
        there area total n order rahul can serve atmost x and ankit can server atmost y

        first sum all rahul order as result and take rahul serve order at n
        ankit_order server order is 0

        take dif_arr
        then loop until n:
            store diff a[n-1] - b[n-1] in heap diff_arr


        while ankit_order < y:
            ele = -(pop element from dif_arr heap)

            if ele < 0:
                that mean rahul tip is greater it will be taken from rahul tip
                but rahul_order > x :
                    then it should be taken from ankit_order
                    result = result + ele
                    decrement rahul_order
                    increment ankit_order
                else:
                    all order are finished
                    break



            else:
                that means tip of ankit is greater so
                add diff in result
                result = result + ele
                increment ankit_order
                decrement rahul_order



    dynamic programming:

        we use naive recursive approach to calculate all possible combination n tip for rahul and ankit and take maximum of it

        to memoized we store key as n+'.'+x+'.'+y and value so that if that combination come we directly take from map

        base case is
        if n=0: return 0


        recursive case
        if x!= 0 and y != 0:
            return max(a[n-1]+self.recur(a,b,n,x-1,y), b[n-1]+self.recur(a,b,x,y-1))

        if y==0:
            return a[n-1] + self recursion for a
        else:
            return b[n-1] + self recursion for b




"""





import heapq


class Solution:

    def maxTip(self, a, b, n, x, y):
        # code here

        max_tip = 0
        rahul_order = n
        ankit_order = 0
        diff_arr = []
        result = sum(a)

        while n:
            heapq.heappush(diff_arr, a[n-1]-b[n-1])
            n = n-1

        print("diff_arr, result", diff_arr, result)

        while ankit_order < y :
            value = -heapq.heappop(diff_arr)
            print("current value", value)
            if value < 0:
                if rahul_order > x:
                    result = result + value
                    ankit_order = ankit_order + 1
                    rahul_order = rahul_order - 1
                else:
                    break
            else:
                result = result + value
                ankit_order = ankit_order + 1
                rahul_order = rahul_order - 1
                print("result after adding value, ankit_order, rahul_order", result, ankit_order, rahul_order)

        return result





# dynamic programming:


def recur(self, a, b, n, x, y, dp):

        key = str(n) + '.' + str(x) + '.' + str(y)

        if key in dp:
            return dp[key]

        if n == 0:
            return 0

        if x!=0 and y!=0:
            dp[key] = max(a[n-1]+self.recur(a,b,n-1,x-1,y, dp),
                        b[n-1]+self.recur(a,b,n-1,x,y-1, dp))
            return dp[key]

        if y==0:
            dp[key] = a[n-1] + self.recur(a,b,n-1,x-1, y, dp)
            return dp[key]

        else:
            dp[key] = b[n-1]+ self.recur(a,b, n-1, x, y-1, dp)
            return dp[key]



    def maxTip(self, a, b, n, x, y):
        # code here

        result = 0
        dp = {}
        result = self.recur(a,b,n,x,y,dp)
        return result
