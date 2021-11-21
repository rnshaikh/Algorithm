
"""

    st =  "bbabcbaaa"


    problem substructure :

        if there is only one char then it palindrome





"""






class Palindrome:

    def __init__(self):
        pass


    def solution(self, st):

        start = 0
        end = 0
        max_length = 0

        for i in range(0, len(st)):

            for j in range(i, len(st)):
                i_temp = i
                j_temp = j
                flag = 1
                while(j_temp>=i_temp):
                    if st[i_temp] != st[j_temp]:
                        flag = 0
                    j_temp = j_temp -1
                    i_temp = i_temp+1

                if flag == 1 and max_length < len(st[i:j+1]):
                    start = i
                    end = j+1
                    max_length = len(st[i:j+1])

        return st[start:end]

    def dynamic(self, st):

        import pdb
        pdb.set_trace()
        dp = [[0 for _ in range(len(st))] for _ in range(len(st))]

        max_length = -1
        start = 0
        end = 1

        for i in range(len(st)-1, -1, -1):
            for j in range(i, len(st)):
                if i == j:
                    dp[i][j] = 1

                elif st[i] == st[j]:
                    if j-i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j-i>=max_length:
                    max_length = j-i
                    start = i
                    temp_j = j
                    end = temp_j + 1
        import pdb
        pdb.set_trace()
        return st[start:end]



s = "dd"
pal = Palindrome()
print(pal.dynamic(s))
