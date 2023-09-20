

"""
1) Optimal Substructure: 
Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of the longest palindromic subsequence of X[0..n-1]. 
If last and first characters of X are same, then L(0, n-1) = L(1, n-2) + 2. 
Else L(0, n-1) = MAX (L(1, n-1), L(0, n-2)). 

Following is a general recursive solution with all cases handled. 

// Every single character is a palindrome of length 1
L(i, i) = 1 for all indexes i in given sequence

// IF first and last characters are not same
If (X[i] != X[j])  L(i, j) =  max{L(i + 1, j),L(i, j - 1)} 

// If there are only 2 characters and both are same
Else if (j == i + 1) L(i, j) = 2  

// If there are more than two characters, and first and last 
// characters are same
Else L(i, j) =  L(i + 1, j - 1) + 2 

"""




"""
same as longest common subsequence
but solution given is dp

"""



class Solution:

    def longestPalinSubseq(self, S):
        # code here
    
        n = len(S)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        
        for gap in range(2, n+1):
            for i in range(n-gap+1):
                j = i+gap-1
                
                if S[i] == S[j] and gap==2:
                    dp[i][j] = 2
                elif S[i] == S[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]