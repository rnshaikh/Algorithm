"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time.
"""

"""
    same as covid infect probleme we can solved it by using bfs

"""


class Solution:

    #Function to find minimum time required to rot all oranges.

    def is_valid(self, row, col, x, y):
        if(x >=0 and x<row and y>=0 and y<col):
            return True
        return False


    def orangesRotting(self, grid):
        #Code here
        row = len(grid)
        col = len(grid[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        queue = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append([i, j])

        timer = -1
        while(len(queue)):
            length = len(queue)
            while(length > 0):
                index = queue.pop(0)
                print("index", index)
                for i in range(len(dx)):
                    x = index[0] + dx[i]
                    y = index[1] + dy[i]
                    print("x, y", x, y)
                    if(self.is_valid(row, col, x, y) and grid[x][y] == 1):
                        grid[x][y] = 2
                        queue.append([x, y])
                length = length - 1
                print("length after decrement and queue", length, queue)
            timer = timer + 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return timer


sol = Solution()
grid = [[0,1,2], [0,1,2], [2,1,1]]
print(sol.orangesRotting(grid))
