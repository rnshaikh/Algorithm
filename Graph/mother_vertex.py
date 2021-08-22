# mother vertex is vertex from where all vertex has path

"""

    use dfs for all vertex in loop
    takes last vertex as finish vertex: vertex whose all descendant are visited
    again initializd visited list
    again call dfs from finish vertex
    if all visited is True then its mother vertex else return -1

"""
