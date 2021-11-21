
# knapscak problem

"""
    Knapsack problem : weight W of knapsack is given
    there n element with value, weight

    we have push element in knapsack suck sum of values of element should be maximum and sum of weight of element
    should be less than or equal to capacity of knapsack W

    so here we are going to use dynmic programming.

    optimal sub structure is : if current element is present or not

    if current element is present then current optimal value and capacity is a[i-1, x-wi] + current value : here were adding value in last value and reducing capacity by current element wieght
    if current elemnt is not present then current optimal value and capacity is a[i-1, x] . here were taking last value and capacity as we are not adding current element
    whatever maximum is stored in a[i][x]

    optimal value in knapsack will last element in array


    to print actual element we have reconstruct it from top down from last element

    if last value is not present in knapsack a[i-1][x] == a[i][x]:
        i = i-1

    else if last value is present then
        print(element)
        i = i-1
        x = x-wi

"""



class knapsack:


    def __init__(self, w, n):
        self.w = w
        self.n = n

    def dynamic(self, ele):

        import pdb
        pdb.set_trace()
        ai = [[0 for i in range((self.w+1))] for j in range((self.n+1))]

        for i in range(1, self.n+1):
            for x in range(0, self.w+1):
                ele_not_present = ai[i-1][x]
                ele_present = 0

                if x-ele[i-1][1] >= 0:
                    ele_present = ai[i-1][x-ele[i-1][1]] + ele[i-1][0]

                optimal_value = max(ele_not_present, ele_present)
                ai[i][x] = optimal_value

        import pdb
        pdb.set_trace()
        print("Optimal value present in knapsack:", ai[-1][-1])

        i = self.n
        x = self.w

        print("element are : ")
        while i >=0:

            if ai[i-1][x] == ai[i][x]:
                i = i-1

            else:
                print(ele[i-1][0], ele[i-1][1])
                i = i-1
                x = x-ele[i-1][1]


if __name__ == "__main__":


    kn = knapsack(6,4)

    element = [[3,4], [2,3], [4,2], [4,3]]

    kn.dynamic(element)








