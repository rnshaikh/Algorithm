"""
    Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

"""

"""
    we can check two words are anagram by sorting them check if string is equal or not
    using merge sort we can do than in O(n log n) time
    so here traverse word
        sort it
        if it present in hashmap then jush append current word in list
        else:
            hashamp[sort_word] = [word]

        return hashmap.values() as answer


    or

    there is 25 char from a-z
    count char in word as tuple store in default dict in that tuple



"""




class Solution:


    def divide(self, word_arr):

        if len(word_arr) > 1:

            mid = len(word_arr) // 2

            left = word_arr[:mid]
            right= word_arr[mid:]
            self.divide(left)
            self.divide(right)

            self.conquer(word_arr, left, right)


    def conquer(self, word_arr, left, right):

        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):

            if left[i] < right[j]:
                word_arr[k] = left[i]
                i = i+1
                k = k+1
            else:
                word_arr[k] = right[j]
                j = j+1
                k = k+1

        while(i < len(left)):
            word_arr[k] = left[i]
            i = i+1
            k = k+1

        while(j < len(right)):
            word_arr[k] = right[j]
            j = j+1
            k = k+1

    def sort_word(self, word, hashmap):

        word_arr = list(word)
        self.divide(word_arr)
        sort_word =  "".join(word_arr)
        if sort_word in hashmap:
            arr  = hashmap[sort_word]
            arr.append(word)
            hashmap[sort_word] = arr
        else:
            hashmap[sort_word] = [word]


    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        hashmap = {}

        for word in words:
            self.sort_word(word, hashmap)

        return hashmap.values()
