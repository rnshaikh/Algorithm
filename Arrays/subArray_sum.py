

# Method 1 :

"""
    1) traverse array from first position
    2) sum as current element with index
    3) traverse array from current element +1 to last
    4) add this element in sum
    5) check if sum == s if yes then return i+1, k+1
    6) continue 1st

    o(n2)


"""

class Solution:
    def subArraySum(self,arr, n, s):
        #Your code here

        for i in range(0, n-1):
            sum_obj = arr[i]
            for k in range(i+1, n):
              sum_obj = sum_obj + arr[k]
              if sum_obj == s:
                  return [i+1, k+1]
        return [-1]




"""
    Method 2:

        1) start = 0 sum = arr[0] i=1
        2) traverse until last element i < n
        3) until curr_sum < s  and start less than i-1 then minus start element and increment start by 1
        4)  if curr_sum = s return start+1, i
        5) i<n add current element in curr_sum

"""



class Solution:
    def subArraySum(self,arr, n, sum_):

        curr_sum = arr[0]
        start = 0
        i = 1
        while i <= n:

            while curr_sum > sum_ and start < i-1:

                curr_sum = curr_sum - arr[start]
                start += 1

            if curr_sum == sum_:
                return [start+1, i]

            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1
        return [-1]
