

"""
    prefix_tree:
        each node can have 26 child as there 26 chars
        and end_word true/false to show word is end there or not

"""



class Node:
    def __init__(self):

        self.child = {}
        self.end_word = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.child:
                curr.child[i] = Node()
            curr = curr.child[i]

        curr.end_word = True

    def search(self, word: str) -> bool:

        curr = self.root

        for i in word:
            if i not in curr.child:
                return False
            curr = curr.child[i]

        return curr.end_word


    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for i in prefix:
            if i not in curr.child:
                return False
            curr = curr.child[i]

        return True
