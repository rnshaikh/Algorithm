# count pair of element with sum == k


"""
    initailze count = 0
    dict = {}

    traverse through array

        i=0 , a[i] = 1   x= k -arr[i] = 2-1 = 1, count=0, {}
        x in obj.keys() not present
        arr[i] in obj.keys() not present
        obj[1] = 1

        i=1 a[i] = 1,  x=k-arr[i] = 2-1 =1, count= 0 , {1:1}
        x in obj.keys()  1 is present = count = count + obj[x]  = 0+1 = 1
        arr[i] is presint in obj,keys()  1 is present  obj[1] = obj[1]+1 = 2


        i=2 a[i]=1, x= k-arr[i] = 2-1 =1 , count=1, {1:2}
        x in obj.keys , 1 is present then count = count+ obj[x]  = 1+2 = 3
        arr[i] is present in obj.keys(),  1 is present  obj[1] = obj[1]+1 = 2+1 = 3


        i=3, a[i] =1, x= k -arr[i] = 2-1 =1, count=3, {1:3}
        x in obj.keys, 1 is present then  count = count + obj[x] = 3+3 = 6
        arr[i] is present in obj.keys(), 1 is present obj[1] = ob[1]+1  = 3+1=4

        return count = 6




"""


class Solution:
    def getPairsCount(self, arr, n, k):
        # code here

        import pdb
        pdb.set_trace()

        count = 0
        obj = {};

        for i in range(n):
            x = k -arr[i]

            if x in obj.keys():
                count +=obj[x];
            if arr[i] in obj.keys():
                obj[arr[i]] += 1;
            else:
                obj[arr[i]] = 1

        return count



a = [1, 1, 1, 1]
k = 2
obj = Solution()
print(obj.getPairsCount(a, 4, 2))



        # m = [0] * 1000

        # # Store counts of all elements in map m
        # for i in range(0, n):

        #     index= arr[i]
        #     m[index] = m[index] + 1

        # twice_count = 0

        # # Iterate through each element and increment
        # # the count (Notice that every pair is
        # # counted twice)
        # for i in range(0, n):

        #     twice_count += m[k - arr[i]]

        #     # if (arr[i], arr[i]) pair satisfies the
        #     # condition, then we need to ensure that
        #     # the count is  decreased by one such
        #     # that the (arr[i], arr[i]) pair is not
        #     # considered
        #     if (k - arr[i] == arr[i]):
        #         twice_count -= 1

        # # return the half of twice_count
        # return int(twice_count / 2)



        # linear solution o(n2)
        # count = 0

        # for i in range(n):
        #     sum_a = 0
        #     for j in range(i+1, n):

        #         sum_a = arr[i]+arr[j]

        #         if sum_a == k:
        #             count=count+1

        # return count
