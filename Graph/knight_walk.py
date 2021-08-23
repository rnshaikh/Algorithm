
# knight walk = knight start and target position is given we have to find minimum steps knight can take to reach target postion.

"""
    here we use BFS :
    knight have 8 position he can walk from curr post:

    1) initited visited array with all false
    2) initiate queue
    3) append startpos in queue and mark it visited.
    4) repeat until queue is empty
    5) pop pos from queue check if it is target return dist
    6) else check out 8 which are valid unvisited pos then append in queue with dist+1

"""

class cell:

    def __init__(self, x=0,y=0,dist=0):
        self.x = x
        self.y = y
        self.dist = dist


class Solution:

    def checkValid(self, x, y, visited, N):

        if (x>=1 and x <= N and y>=1 and y<=N):
            return True
        return False

    def minStepToReachTarget(self, knightpos, targetpos, N):
#       #Code here

        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]

        queue = []
        visited = [[False] * (N+1) for _ in range(N+1)]

        startPos = cell(KnightPos[0], KnightPos[1], 0)
        queue.append(startPos)
        visited[KnightPos[0]][KnightPos[1]] = True

        while len(queue):
            curr = queue.pop(0)
            if (curr.x == TargetPos[0] and curr.y == TargetPos[1]):
                return curr.dist

            for i in range(8):
                x = curr.x+dx[i]
                y = curr.y+dy[i]

                if(self.checkValid(x, y, visited, N) and not visited[x][y]):
                    visited[x][y] = True
                    pos = cell(x, y, curr.dist+1)
                    queue.append(pos)
