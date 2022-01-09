"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

"""
    1) sort all intervals in increasing order of starting point:
    2) initialized stack push first interval
    3) loop thorught 1 to last interval
        if top[end] < current[start]:
            just push current into stack (bc not overlapping)

        elif top[end] <current[end]:

            update top[end] = current[end]
            pop stack top
            push current into stack


    return stack
"""





class Solution:


    def divide(self, intervals):

        if len(intervals) > 1:

            mid = len(intervals) // 2

            left = intervals[:mid]
            right = intervals[mid:]

            self.divide(left)
            self.divide(right)
            self.conquer(intervals, left, right)

    def conquer(self, intervals, left, right):

        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):

            if left[i][0]< right[j][0]:
                intervals[k] = left[i]
                i = i+1
                k = k+1
            else:
                intervals[k] = right[j]
                j = j+1
                k = k+1

        while(i < len(left)):
            intervals[k] = left[i]
            i = i+1
            k = k+1

        while(j < len(right)):
            intervals[k] = right[j]
            j = j+1
            k = k+1

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        self.divide(intervals)
        stack = []

        stack.append(intervals[0])

        for i in range(1, len(intervals)):

            top = stack[-1]

            if top[1] < intervals[i][0]:
                stack.append(intervals[i])


            elif top[1] < intervals[i][1]:
                top[1] = intervals[i][1]
                stack.pop(-1)
                stack.append(top)


        return stack

