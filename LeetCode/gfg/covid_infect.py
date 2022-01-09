"""
    Aterp is the head nurse at a city hospital. City hospital contains R*C number of wards and the structure of a hospital is in the form of a 2-D matrix.
Given a matrix of dimension R*C where each cell in the matrix can have values 0, 1, or 2 which has the following meaning:
0: Empty ward
1: Cells have uninfected patients
2: Cells have infected patients

An infected patient at ward [i,j] can infect other uninfected patient at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. Help Aterp determine the minimum units of time after which there won't remain any uninfected patient i.e all patients would be infected. If all patients are not infected after infinite units of time then simply return -1.

"""

"""
    we can use bfs on 2d array to find out in how many time all ward get infected

    first find infected ward push in queue

    while wueue is not empty :
        check it neighbour ward if it is not infected updated it to 2 push queue

        increse timer by 1

    check all ward become infecter if not return -1

    return timer

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
        for i in range(M):
            for j in range(N):
                if hospital[i][j] == 2:
                    queue.append([i,j])
        timer = -1

        while(len(queue)):
            length = len(queue)
            while(length>0):
                curr = queue.pop(0)
                for i in range(4):
                    x = curr[0] + dx[i]
                    y = curr[1] + dy[i]
                    if(self.valid(x,y,M,N) and hospital[x][y] == 1):
                        queue.append([x,y])
                        hospital[x][y] = 2
                length = length-1

            timer = timer+1


        for i in range(M):
            for j in range(N):
                if hospital[i][j] == 1:
                    return -1

        return timer
