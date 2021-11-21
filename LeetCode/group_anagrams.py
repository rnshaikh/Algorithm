"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""



from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_words = defaultdict(list)

        for word in strs:
            group_words["".join(sorted(word))].append(word)

        ans = []

        for key in group_words:
            ans.append(group_words[key])

        return ans



