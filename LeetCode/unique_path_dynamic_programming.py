"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

"""

"""
    algorithm:

        for finding unique path in m*n matrix we can use dynamic programing bottom-up(finish-to-start) approach starting 1 to last cell
        here recursive solution wehave add uniq(m-1, n) + uniq(m, n-1) and base case is if row or col is 1 return 1
        beacuse when row is 1 or col is 1 there only 1 unique path to robot.

        same algorithm can be solve using dynamic programming
        take path[m][n]
        initial is for 0 row and 0 colum insert 1 bc there only unqiue path.
        path[0][0] path[0][1] .... = 1
        path[0][0], path[1][0],... = 1

        loop through 1 to m row
            1 to n col

                path[i][j] = path[i-1][j] + path[1][j-1]


        return path[m-1][n-1]


"""



class Solution:

    def count_unique(self, m, n):
        print("m n",m, n)
        if m==1 or n==1:
            print("m or n:1",m,n)
            return 1

        return self.count_unique(m-1, n) + self.count_unique(m, n-1)


    def uniquePaths(self, m: int, n: int) -> int:

        #return self.count_unique(m, n)

        path = [[0 for _ in range(0, n)] for _ in range(0, m)]

        for i in range(n):
            path[0][i] = 1

        for j in range(m):
            path[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]
