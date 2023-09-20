"""
You are at the side of a river. You are given a m litre jug and a n litre jug where 0 < m < n. Both the jugs are initially empty. 
The jugs don’t have markings to allow measuring smaller quantities. 
You have to use the jugs to measure d litres of water where d < n. 
Determine the minimum no of operations to be performed to obtain d litres of water in one of jug.
The operations you can perform are:

Empty a Jug
Fill a Jug
Pour water from one jug to the other until one of the jugs is either empty or full.

"""


"""
    calculate gcd of n, m if d is divisible  by d then only possible else -1
    if m > n return -1
    if n < d return -1

    else
        find_out steps for 2 cases
        filling = m fill in m pour in n
        empty = n

        2) filling = n  fill in n and pour in m
            empty = m

    min of 2 cases is ans

"""

class Solution:

    def gcd(self, a,b):
        if b==0:
            return a
        return self.gcd(b, a%b)


    def find_min_steps(self, fill, empty, d):

        steps = 0
        from_jug = fill
        to_jug = 0
        steps = steps+1

        while(from_jug != d and to_jug != d):

            rem = min(from_jug, empty-to_jug)

            to_jug += rem
            from_jug -= rem
            steps = steps+1

            if from_jug == d or to_jug == d:
                break

            if from_jug == 0:
                from_jug = fill
                steps = steps+1

            if to_jug==empty:
                to_jug = 0
                steps = steps+1

        return steps


    def minSteps(self, m, n, d):
        # Code here

        gc = self.gcd(m, n)

        if m > n:
            return -1

        if d % gc != 0:
            return -1

        if n < d:
           return -1

        min_step1= self.find_min_steps(n, m, d)
        min_step2= self.find_min_steps(m, n, d)

        #print("min steps", min_step1, min_step2)
        steps = min(min_step1, min_step2)
        return steps
