# max weight independant set in path graph

#Algorithm
"""
    optimal solution : there 2 case if current vertex is part of is. if it then wis[i-2] + weight 
    of current vertex is independant set of
    current else if current vertex is not part of independant set then wis[i-1] is i.s. of current of vertex

    we take max of above case

    as it is dynamic progamming we use bottom-up approach starting from first vertex


    if we want print i.s then
    we can do it in linear from top down from last vertex

    if current vertex is not part of i.s wis[i-1] == w[i]:
        i --
    else : current vertex is part of i.s
        print current vertex
        i = i-2

"""



class WIS:

    def __init__(self):
        pass

    def max_wis(self, graph):

        import pdb
        pdb.set_trace()
        wis = [0] * len(graph)
        wis[0] = graph[0]

        for i in range(0, len(graph)):

            wis_without_last_ver = wis[i-1]
            wis_with_last_ver = wis[i-2] + graph[i]
            curr_wis = max(wis_with_last_ver, wis_without_last_ver)
            wis[i] = curr_wis


        print("Max weight of independant set is :", wis)


if __name__ == "__main__":

   ids = WIS()
   graph = [1,4,5,4]
   ids.max_wis(graph)

