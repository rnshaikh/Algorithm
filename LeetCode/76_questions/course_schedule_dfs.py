

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

"""


"""

    use dfs on every
    vertex and detect cycle
    if vertex dont have neigbhor
    visited = false
    greaph[ver] = []
    in end

"""


from collections import defaultdict

class Solution:

    def dfs_util(self, visited, graph, ver):

        visited[ver] = True

        for ve in graph[ver]:
            if visited[ve] == False:
                if (self.dfs_util(visited, graph, ve)== True):
                    return True
            else:
                return True

        visited[ver] = False
        graph[ver] = []

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])

        visited = [False for _ in range(numCourses)]

        for i in range(numCourses):
            flag = self.dfs_util(visited, graph, i)
            if flag == True:
                return False

        return True
