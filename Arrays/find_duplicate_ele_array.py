
# duplicates element in array

# sort array in asc. if arr[i] is equal to arr[i+1] until n-1

class Solution:
    def duplicates(self, arr, n):
        arr.sort()
        result = []
        for i in range(0, n-1):
            if arr[i] == arr[i+1]:
                if len(result)>0 and arr[i] == result[-1]:
                   continue
                result.append(arr[i])
        return [-1] if len(result)<=0 else result

