"""
Given an infinite number line. You start at 0 and can go either to the left or to the right.
The condition is that in the ith move, youmust take i steps. Given a destination D ,
find the minimum number of steps required to reach that destination.
"""

"""
the logic behind this problem is that we keep adding the number till 
either we get our target of we hit greaer than target...
Now, let's take some examples.
D = 1 (1 steps)
D = 2 (1 + 2) which is greater than 2 now we keep adding element till sum > target and (sum-target)%2 == 0) because
      (1 + 2 + 3) here 6 - 4 = 2 so we will stop here... the logic here is if we turn +2 to -2 (1 -2 + 3) we will get 2...so we will be ultimately substracting 2*i from
      out sum....

"""

class Solution:
    def minSteps(self, D):
        # code here

        D = abs(D)
        curr_pos = 0
        steps = 0

        while(True):
            curr_pos = curr_pos + steps
            steps = steps+1
            if curr_pos == D:
                return steps-1
                break;
            if curr_pos > D and (curr_pos-D)%2 == 0:
                return steps-1
                break;
        return 0
