
# Counting elements in two arrays


# count elements in 2nd array which less then or equal element in 1st array


# Method 1 linear

result = []
for i in range(n1):

    count = 0
    for j in range(n2):

        if arr2[j] <= arr1[i]:
            count = count+1

    result.append(count)

return result



# method2 : sort arr2, then do binary search for each element 1st array. which find largest index of element >= element in 1st array


def binary(self, arr, n, ele):

        l = 0
        h = n-1
        while(l <= h):
            mid = int((l+h)/2)
            if arr[mid] <= ele:
                l = mid+1

            else:
                h = mid - 1
        return h


def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
    #returns the required output
    arr2.sort()
    for i in range(n1):
        index = self.binary(arr2,n2, arr1[i])
        arr1[i] = index+1
    return arr1
