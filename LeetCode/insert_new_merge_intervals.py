"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

"""

"""
    there are 3 cases

    1. if new intervals comes before current interval then append new interval in result and add intervals[i:]  new[1] < curr[0]

    2. if new interval comes after current interval then append curr interval : new[0] > curr[1]

    3. else. it is overlapping then update newinterval with min(new[0], curr[0]) max(new[1], curr[1])

    last
        merge new interval



"""




class Solution:


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new = newInterval
        n = len(intervals)

        result = []


        for i in range(n):

            if new[1] < intervals[i][0]:
                result.append(new)
                return result + intervals[i:]

            elif new[0] > intervals[i][1]:
                result.append(intervals[i])

            else:
                new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]

        result.append(new)

        return result
