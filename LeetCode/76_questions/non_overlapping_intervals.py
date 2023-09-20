"""

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



"""


"""
    1) sort intervals
    2) check if interval overlapping if prev_end >= current start of interval then not ovarlapping else overlapping
    3) if overlapping remove interval whose end is greater
    4) increment count

"""


class Solution:


    def divide(self, intervals):

        if len(intervals)>1:

            mid = len(intervals)//2

            left = intervals[:mid]
            right = intervals[mid:]

            self.divide(left)
            self.divide(right)
            self.conquer(intervals, left, right)


    def conquer(self, intervals, left, right):

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i][0] <= right[j][0]:
                intervals[k] = left[i]
                i = i+1
                k = k+1
            else:
                intervals[k] = right[j]
                j = j+1
                k = k+1

        while i < len(left):
            intervals[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            intervals[k] = right[j]
            j = j+1
            k = k+1


    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        self.divide(intervals)


        cnt = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0]>=prev_end:
                prev_end = intervals[i][1]
            else:
                cnt = cnt+1
                prev_end = min(intervals[i][1], prev_end)

        return cnt


