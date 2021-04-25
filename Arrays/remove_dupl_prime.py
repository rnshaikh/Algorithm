# Remove duplicates in small prime array


class Solution:
    def removeDuplicates(self, arr):
        # code here

        hash_arr = []


        for i in arr:

            if i in hash_arr:
                continue

            hash_arr.append(i)

        return hash_arr



