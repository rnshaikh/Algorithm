"""
Aterp is the head nurse at a city hospital. City hospital contains R*C number of wards and the structure of a hospital is in the form of a 2-D matrix.
Given a matrix of dimension R*C where each cell in the matrix can have values 0, 1, or 2 which has the following meaning:
0: Empty ward
1: Cells have uninfected patients
2: Cells have infected patients

An infected patient at ward [i,j] can infect other uninfected patient at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1]
(up, down, left and right) in unit time. Help Aterp determine the minimum units of time after which there won't remain
any uninfected patient i.e all patients would be infected. If all patients are not infected after infinite units of time
then simply return -1.

"""

"""
    find unit of time required to beacome all uninfected patients become infected 1 unit is one loop .
    1) take queue for bfs and timer = -1.
    2) push all infected ward to queue
    3) repeat while queue is not empty
    4) take length of queue and repeat until it not 0 it 1 loop for 1 unit
    5) pop pos from queue check validity of all 4 possible position if true push into queue make pos infected =2
    6) length become zero increment timer
    7) check if there is any uninfected ward if yes return 1
    8) else return timer

"""




class Solution:

    def valid(self, x, y, M, N):
        if(x>=0 and x<M and y>=0 and y<N):
            return True
        return False

    def helpaterp(self, hospital):
        # code here
        queue = []

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        M = len(hospital)
        N = len(hospital[0])
        for i in range(len(hospital)):
            for j in range(len(hospital[i])):
                if hospital[i][j] == 2:
                    queue.append([i,j])

        timer = -1

        while(len(queue)):
            import pdb
            pdb.set_trace()
            length = len(queue)
            while(length>0):
                import pdb
                pdb.set_trace()
                curr = queue.pop(0)
                for i in range(4):
                    x = curr[0] + dx[i]
                    y = curr[1] + dy[i]
                    if(self.valid(x,y,M,N) and hospital[x][y] == 1):
                        queue.append([x,y])
                        hospital[x][y] == 2
                length = length-1

            timer = timer+1

        for i in range(M):
            for j in range(N):
                if hospital[i][j] == 1:
                    return -1

        return timer



if __name__ == "__main__":

    si = Solution()
    hospital = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
    print(si.helpaterp(hospital))
