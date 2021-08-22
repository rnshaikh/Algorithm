## from path from source 1 to destination 2  0 meanins wall can't have path, can move from left, right, top, bottom

"""
    method:
        1) m = length of grid m = width of grid
        2) traverse and find out source 1's index p, q
        3) if p and q call dfs with grid, x, y, m, n
        4) exit condition if x<0 or x>=m same for y or grid[x][y] = 0 or flag=1 then return
        5) check if grid[x][y] == 2 update flag == 1 return
        6) call 4 combination of dfs

"""

class Solution:

    #Function to find whether a path exists from the source to destination.
    def __init__(self):
        self.flag = 0

    def dfs_util(self, grid, x, y, m, n):

        if(x<0 or x>=m or y<0 or y>=n or grid[x][y]==0 or self.flag==1):
            return

        if grid[x][y] == 2:
            self.flag = 1
            return

        grid[x][y] = 0

        self.dfs_util(grid, x+1, y, m, n)
        self.dfs_util(grid, x-1, y, m, n)
        self.dfs_util(grid, x, y+1, m, n)
        self.dfs_util(grid, x, y-1, m, n)



    def is_Possible(self, grid):
        #Code here
        m = len(grid)
        n = len(grid[0])
        p = None
        q = None

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    p = i
                    q = j
                    break

        if p or q or p==0 or q==0:
            self.dfs_util(grid, p, q, m, n)
        return self.flag



#{
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.is_Possible(grid)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
