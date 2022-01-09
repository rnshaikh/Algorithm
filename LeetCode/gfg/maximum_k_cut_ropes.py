"""
    Given an array arr[] consisting of N positive integers representing the lengths of N ropes and a positive integer K,
    the task is to find the maximum length of the rope that has a frequency of at least K by cutting any ropes in any number of pieces.

"""

"""
    here we can use binary search
    take low = 1
    high = maximum element in array
    ans = -1

    iterate untile low <= high

        mid =  calculate mid
        count = 0
        traverse through each element
            increment count by dividing element by mid

        if count >= k
            update ans
            update low as mid+1
        else:
            update high as mid-1

"""


class Ropes:

    def __init__ (self, arr, k):
        self.arr = arr
        self.k = k

    def find_max(self):

        max_ele = -9999999999

        for i in  arr:
            if max_ele < i:
                max_ele = i

        return max_ele

    def maximum_roes(self):

        low = 1
        high = self.find_max()
        print("high", high)
        ans = -1

        while(low <= high):
            mid = (low + high) // 2
            print("mid", mid)
            count = 0

            for i in range(len(arr)):
                count = count + arr[i] // mid

            if count >= k:
                ans = count
                low = mid+1
            else:
                high = mid-1

        return ans




arr = [5, 2, 7, 4, 9]
k  = 5

obj = Ropes(arr, k)
print("maximum length of rope cut atleast k :", obj.maximum_roes())



# Python program for the above approach

# Function to find the maximum size
# of ropes having frequency at least
# K by cutting the given ropes
def maximumSize(a, k):

    # Stores the left and
    # the right boundaries
    low = 1
    high = max(a)

    # Stores the maximum length
    # of rope possible
    ans = -1

    # Iterate while low is less
    # than or equal to high
    while (low <= high):

        # Stores the mid value of
        # the range [low, high]
        mid = low + (high - low) // 2

        # Stores the count of ropes
        # of length mid
        count = 0

        # Traverse the array arr[]
        for c in range(len(a)):
            count += a[c] // mid


        # If count is at least K
        if (count >= k):

            # Assign mid to ans
            ans = mid

            # Update the value
            # of low
            low = mid + 1

        # Otherwise, update the
        # value of high
        else:
            high = mid - 1

    # Return the value of ans
    return ans

# Driver Code
if __name__ == '__main__':
    arr = [5, 2, 7, 4, 9]
    K = 5
    print(maximumSize(arr, K))

# This code is contributed by mohit kumar 29.
