"""
    There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

    Given the array answers, return the minimum number of rabbits that could be in the forest.

"""

"""

    here we have to determined how many groups are there and each group how many rabbits are there?

    for this take hash_map and count 0

    traverse each element in array
        if element is not present in hashmap or hash_map[element] is zero that means it is new group:
            increment count by (element value + 1)
            store element value+1 as hash_map[ele]

        decrement hash_map[element] by 1 as 1 rabbit ans the que.


 """



class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count = 0
        hash_map = {}

        for i in range(len(answers)):

            if answers[i] not in hash_map or hash_map[answers[i]] == 0:
                count = count + (answers[i]+1)
                hash_map[answers[i]] = answers[i]+1

            hash_map[answers[i]] = hash_map[answers[i]]-1

        return count


