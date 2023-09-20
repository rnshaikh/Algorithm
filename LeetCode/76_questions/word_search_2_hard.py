"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

"""

"""
    first create prefix tree for list of words

    then traverse each row col position in board call dfs with board, currrow, currcol, node, wordsofoar

    in dfs check exit case for row col if char not in prefix tree

    add char to word
    change node to curr char
    temp = curr char
    board[row][col] = None

    if it is end_word:
        add to resul
        make end_word false

    call dfs for neighbour

    unset board[row][col] = temp


"""



class TrieNode:
    def __init__(self):
        self.childern = {}
        self.end_word = False

class Solution:
    def __init__(self):

        self.root = TrieNode()
        self.res = []

    def addword(self, word):

        temp = self.root

        for w in word:
            if w not in temp.childern:
                temp.childern[w] = TrieNode()
            temp = temp.childern[w]

        temp.end_word=True

    def dfs(self, board, row, col, m, n, node, word):

        if row< 0 or row>=m or col < 0 or col>=n or board[row][col] not in node.childern:
            return

        node = node.childern[board[row][col]]
        word = word + board[row][col]
        temp = board[row][col]
        board[row][col] = None

        if node.end_word:
            self.res.append(word)
            node.end_word=False

        self.dfs(board, row+1, col, m, n, node, word)
        self.dfs(board, row, col+1, m, n, node, word)
        self.dfs(board, row-1, col, m, n, node, word)
        self.dfs(board, row, col-1, m, n, node, word)
        board[row][col] = temp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        for word in words:
            self.addword(word)

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, m, n, self.root, "")
        return self.res
