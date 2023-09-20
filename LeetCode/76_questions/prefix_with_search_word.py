

"""
    build brefix tree
    in search
    word

    normal search is same as prefix tree

    only . for next char you have search for all child of curr node using dfs


"""



class Node:

    def __init__(self):

        self.child = {}
        self.end_word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:

        curr = self.root

        for i in word:
            if i not in curr.child:
                curr.child[i] = Node()
            curr = curr.child[i]

        curr.end_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for ch in curr.child.values():
                        if dfs(i+1, ch):
                            return True
                    return False

                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]

            return curr.end_word

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
