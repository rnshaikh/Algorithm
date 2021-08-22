# snakes and ladders problem

"""
Given a 5x6 snakes and ladders board, find the minimum number of dice throws required to reach the destination or last cell (30th cell) from the source (1st cell).
You are given an integer N denoting the total number of snakes and ladders and an array arr[] of 2*N size where 2*i and (2*i + 1)th values
denote the starting and ending point respectively of ith snake or ladder. The board looks like the following.
"""


"""
    1) seprate out ladders , snakes postion from arr, if N=8 there area 2*N values in arr
    2) initialize queue with lenght, value, 0,1
    3) while queue is not empty
    4) pop length , value
    3) if value == 30 return length
    4) for i in range(1, 7) for ludo value 1, 6
    5) if value+i <= 30:
    6) if value+i in ladder key then append length+1, ladders[value+i]
    7) if it is in snakes continue
    8) else append length+1, value+i
    9) if not found length return -1

"""


class Solution:
    def minThrow(self, N, arr):
        # code here

        ladders = {}
        snakes = {}

        loop = N
        for i in range(0, 2*N, 2):

            if arr[i]<arr[i+1]:
                ladders[arr[i]] = arr[i+1]
            else:
                snakes[arr[i]] = arr[i+1]

        queue= []
        queue.append((0,1))
        while(queue):

            length, value = queue.pop(0)
            if value==30:
                return length

            for i in range(1, 7):
                if value+i <=30:
                    if value+i in snakes:
                        continue
                    elif value+i in ladders:
                        queue.append((length+1, ladders[value+i]))

                    else:
                        queue.append((length+1, value+i))



        return -1
