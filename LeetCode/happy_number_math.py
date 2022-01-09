"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

"""



"""
    do calculate happy number
    if == 1 return true
    if it is already occure return false
    aadd in set


"""






class Solution:

    def num_square(self, n):

        num_str = str(n)
        result = 0

        for i in num_str:
            result = result + int(i)*int(i)

        return result


    def isHappy(self, n: int) -> bool:

        st=set()
        while True:

            n = self.num_square(n)
            if n==1:
                return True

            if n in st:
                return False

            st.add(n)
