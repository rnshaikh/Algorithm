# find word in dictionary in board can go in adjancent cell only top, bottom, right, left, diagonal if word form by this postion matches then include in result


"""
    1) for every word in dict
    2) take m = height, n=width wordindex=0, visited 2s array
    3) travers through i, j though m and n
    4) check if baord[i][j] == word[wordindex] first character if true
    5) call dfs with board,i,j,m,n,visited, wordindex
    6) in dfs exit condition is if word_index == len(word) that means all character in word we got return True
    7) else check x is in between 0 to m and y between 0 to n visited[x][y] is False and board[x][y] = word[word_index]
    8) if yes marked visited[x][y] = True and call dfs for all 8 combination of x, y postion for next word in condtion.
    9) if return true : return true
    10) else marke position x,y unvisisted visited[x][y] == 0


"""


class Solution:

    def dfs_util(self,word, board,x,y,m,n,word_index,visited):

        if (word_index == len(word)):
            return True


        if(x>=0 and x<m and y>=0 and y<n and visited[x][y]==False and
           board[x][y] == word[word_index]):
            visited[x][y]=True
            if(
                self.dfs_util(word,board,x-1,y,m,n,word_index+1,visited) or
                self.dfs_util(word,board,x,y-1,m,n,word_index+1,visited) or
                self.dfs_util(word,board,x+1,y,m,n,word_index+1,visited) or
                self.dfs_util(word,board,x,y+1,m,n,word_index+1,visited) or
                self.dfs_util(word,board,x-1,y-1,m,n,word_index+1,visited) or
                self.dfs_util(word,board,x+1,y+1,m,n,word_index+1,visited) or
                self.dfs_util(word,board,x-1,y+1,m,n,word_index+1,visited) or
                self.dfs_util(word,board,x+1,y-1,m,n,word_index+1,visited)
            ):
                    print("Found ", word_index, board[x][y], word[word_index])
                    return True
            visited[x][y] = False

        return False


    def find_word(self, word, board):

        m = len(board)
        n = len(board[0])
        word_index = 0
        visited = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[word_index]:
                    print("Word comparision", board[i][j], word[word_index])
                    if(self.dfs_util(word,board,i,j,m,n,word_index,visited)==True):
                        return True

        return False




    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        res = []
        for word in dictionary:
            if(self.find_word(word, board)):
                res.append(word)

        return res



if __name__ == "__main__":

    so = Solution()
    dictionary = ["CAT"]

    board = [[0]*3 for _ in range(3)]

    board[0][0] = "C"
    board[0][1] = "A"
    board[0][2] = "P"
    board[1][0] = "A"
    board[1][1] = "N"
    board[1][2] = "D"
    board[2][0] = "T"
    board[2][1] = "I"
    board[2][2] = "E"

    print(so.wordBoggle(board, dictionary))


