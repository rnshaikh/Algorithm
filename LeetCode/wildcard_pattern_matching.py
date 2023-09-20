"""
Given two strings 'str' and a wildcard pattern 'pattern' of length N and M respectively,  
You have to print '1' if the wildcard pattern is matched with str else print '0' .

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

Note: The matching should cover the entire str (not partial str).

"""


"""
    algorithm similiar to regular expression matching but here no preceding element match with * . all chars can match for
    that if we use * then condition will i < len(string) and (i+1, j)

"""





class Solution:
    def wildCard(self,pattern, string):
        # Code here

        cache = {}
        def backtracking(i, j):

            if (i,j) in cache:
                return cache[(i,j)]

            if i >= len(string) and j >= len(pattern):
                return 1

            if j >= len(pattern):
                return 0

            match = (i < len(string) and (string[i] == pattern[j] or pattern[j] == "?"))

            if pattern[j] == "*":

                cache[(i,j)] = (backtracking(i, j+1) or
                                (i < len(string) and backtracking(i+1, j)))
                return cache[(i,j)]

            if match:
                cache[(i,j)] = backtracking(i+1, j+1)
                return cache[(i,j)]
            else:
                cache[(i,j)] = 0
                return cache[(i,j)]

        return backtracking(0, 0)



# int wildCard(string p,string s){
#        int n=p.length();
#        int m=s.length();
#        bool dp[n+1][m+1];

#        for(int i=0; i<=n; i++){
#            for(int j=0; j<=m; j++){
#                if(i==0&&j==0) dp[i][j]=true;
#                else if(i==0) dp[i][j]=false;
#                else if(j==0){
#                    if(p[i-1]=='*'){
#                        dp[i][j]=dp[i-1][j];
#                    }
#                    else dp[i][j]=0;
#                }
#                else if(p[i-1]=='?'||p[i-1]==s[j-1]) dp[i][j]=dp[i-1][j-1];
#                else if(p[i-1]=='*') dp[i][j]=dp[i-1][j]||dp[i][j-1];
#                else dp[i][j]=0;
#            }
#        }
#        return dp[n][m];
#    }
