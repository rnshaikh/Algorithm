
"""
Given a sequence of moves for a robot. Check if the sequence is circular or not.

A sequence of moves is circular if the first and last positions of the robot are the same. A move can be one of the following :
    G - Go one unit
    L - Turn left
    R - Turn right

"""


class Solution:

    def isCircular(self, path):
        # code here

        N=1
        S=2
        E=3
        W=4
        curr_dir = 1
        x=0
        y=0

        for i in path:

            if i == "G":
                if curr_dir == 1:
                    y +=1
                elif curr_dir == 2:
                    y -=1
                elif curr_dir == 3:
                    x +=1
                else:
                    x-=1

            elif i == "L":

                if curr_dir == 1:
                    curr_dir =3

                elif curr_dir == 2:
                    curr_dir = 4

                elif curr_dir == 3:
                    curr_dir =2

                else:
                    curr_dir = 1

            elif i == "R":
                if curr_dir == 1:
                    curr_dir = 4

                elif curr_dir == 2:
                    curr_dir = 3

                elif curr_dir == 3:
                    curr_dir = 1

                else:
                    curr_dir = 2

        if x == 0 and y==0:
            return "Circular"

        else:
            return "Not Circular"
