"""
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence
of the given array such that the integers in the subsequence are sorted in increasing order.
 For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100),
 if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input
 array is {10, 5, 4, 3}, then output should be 10

"""



"""
    algorithm dynamic programing bottom-up approach
    tak dp with n element all element at their respective index

    optimal substructure is
        LIS(i) = 1 + LIS(j) where j < i and arr[j] < arr[i]
        else:
        LIS(i) = 1 if no such j exists

    so here outer loop start 1 to n
        j 0 to i
            if arr[i] > arr[j] and dp[i] < arr[i]+dp[j]:
                dp[i] = arr[i] + dp[j]

    then find maximum sum in dp


"""



def maxSumIS(arr, n):
    max = 0
    msis = [0 for x in range(n)]

    # Initialize msis values
    # for all indexes
    for i in range(n):
        msis[i] = arr[i]

    # Compute maximum sum
    # values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and
                msis[i] < msis[j] + arr[i]):
                msis[i] = msis[j] + arr[i]

    # Pick maximum of
    # all msis values
    for i in range(n):
        if max < msis[i]:
            max = msis[i]

    return max


# Maximum sum of elements not part of LIS
# find longest in  increasing squence with min sum subtract it from sum_all

class Solution:
    def maxSumLis(self, Arr, n):
        # code here

        dp = [1 for _ in range(n)]
        sum_a = [0 for i in range(n)]
        sum_all = 0

        for i in Arr:
            sum_all = sum_all+i

        for i in range(n):
            sum_a[i] = Arr[i]

        for i in range(1, n):
            for j in range(0, i):
                if Arr[i] > Arr[j]:
                    if dp[i] < 1+dp[j]:
                    #and dp[i] < dp[j]+1:
                        dp[i] = 1+dp[j]
                        sum_a[i] = sum_a[j] + Arr[i]
                    elif dp[i] == 1+dp[j]:
                        sum_a[i] = min(sum_a[i], sum_a[j]+Arr[i])

        maxi = -10
        sum_max = -10

        for i in range(n):
            temp = maxi
            maxi = max(maxi, dp[i])
            if temp == dp[i]:
                sum_max = min(sum_max, sum_a[i])
            else:
                sum_max = max(sum_max, sum_a[i])

        #print("dp, sum_a", dp, sum_a, sum_all, maxi, sum_all-sum_max)

        return sum_all - sum_max
        # else:
        #     return sum_all-sum_a[-1]

        # totalSum = 0

        # # Find total sum of array
        # for i in range(n):
        #     totalSum += arr[i]

        # # Maintain a 2D array
        # dp = [[0] * n for i in range(2)]

        # for i in range(n):
        #     dp[0][i] = 1
        #     dp[1][i] = arr[i]

        # # Update the dp array along
        # # with sum in the second row
        # for i in range(1, n):
        #     for j in range(i):
        #         if (arr[i] > arr[j]):

        #             # In case of greater length
        #             # update the length along
        #             # with sum
        #             if (dp[0][i] < dp[0][j] + 1):
        #                 dp[0][i] = dp[0][j] + 1
        #                 dp[1][i] = dp[1][j] + arr[i]

        #             # In case of equal length
        #             # find length update length
        #             # with minimum sum
        #             elif (dp[0][i] == dp[0][j] + 1):
        #                 dp[1][i] = min(dp[1][i],
        #                               dp[1][j] +
        #                                  arr[i])

        # maxm = 0
        # subtractSum = 0

        # # Find the sum that need to
        # # be subtracted from total sum
        # for i in range(n):
        #     if (dp[0][i] > maxm):
        #         maxm = dp[0][i]
        #         subtractSum = dp[1][i]

        #     elif (dp[0][i] == maxm):
        #         subtractSum = min(subtractSum,
        #                           dp[1][i])
        # print("dp", dp)
        # # Return the sum
        # return totalSum - subtractSum
