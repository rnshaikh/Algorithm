"""
Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words.
Note: From the dictionary B each word can be taken any number of times and in any order.
"""


"""
    here we have to brak complete line in to meaning ful words which in dictionary

    we can here use dp programming

    take dp with size of len(line)+1
    dp[0] = 1 for base case

    traverse from starting word to last word:

        if not dp[start]  that means if last word is not end hear then take next start
            continue

        travesrse from start+1 to last in line:

            check if [start:end] is word in dict:
                dp[end] = 1  last word is end at 1


    dp[n]


"""




def wordBreak(line, dictionary):
    # Complete this function

    n = len(line)

    dp =  [0 for _ in range(n+1)]

    dp[0] = 1

    for start in range(n+1):

        if not dp[start]:
            continue

        for end in range(start+1, n+1):

            if line[start:end] in dictionary:
                dp[end] = 1

    return dp[n]
