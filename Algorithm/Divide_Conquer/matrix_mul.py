
"""
    in matrix multiple :
    a[i][j]*b[i][j] = all k 0 to n  a[i][k] * b[k][j]


    in naive approach :
        for 2 by 2 matrix there 8 product which we have to compute
    time complexity of naive approach is O(n3)


    in divide conquer approach:
        we divide matrix in n/2 n/2 quadrant
        then we perform multiplication of each quadrant (8)
        then we added to give result.
        but this also has time conplexity O(n3) which is same as naive
        beacasue here also we calculating 8 products

    Strassen Multiplication:
        In strassen multiplication is also divide and conquer design
        but here we calculate only 8 product so
        time complexity is reduced to O(n2)

        let example x=[[A, B],[C,D]]  y=[[E,F],[G,H]]

        7 product are:
        P1 = A(F-H)
        p2 = (A+B)H
        p3 = (C+D)E
        p4 = D(C-E)
        p5 = (A+D)(E+H)
        p6 = (B-D)(C+H)
        p7 = (A-C)(E+F)

        x.y = [p5+p4-p2+p6, p1+p2]
              [p3+p4, p1+p5-p3-p7]
        takes 7 recursive call

"""


class MatMul:

    def __init__(self):
        pass

    def naive(self, A,B):

        result = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(A)):
                    result[i][j] = result[i][j] + A[i][k] * B[k][j]

        print("Multiplication is :", result)

if __name__ == "__main__":

    inv = MatMul()

    A = [[1,2], [3, 4]]
    B = [[2,4], [5,6]]
    inv.naive(A, B)
    inv.divide(A, B)
