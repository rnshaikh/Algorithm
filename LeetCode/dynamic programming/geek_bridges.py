"""
Geek wants to build bridges between two banks of a river to help migrants to reach their homes. But, he can build a bridge only between two similar posts. Bridges can't overlap. The task is to find the maximum number of bridges geek can build.

Note: Each of the posts is represented by either '*' or '@' or '#'.

Example: Let str1 = "*@#*", str2 = "*#". Then output will be 2.
* @ # *
|     /
*  #

"""



"""
    in recursive soltuin if current is is same than 1 + (next character)
    else:
        max(+1, j or i, j+1)

"""




def find(str1, str2):

    n = len(str1)
    m = len(str2)

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


if __name__ == "__main__":

    n = int(input(""))
    ans = []
    while n > 0:
        str1, str2 = input("").split(" ")
        bridges = find(str1, str2)
        ans.append(bridges)
        n = n-1

    for i in ans:
        print(i)
