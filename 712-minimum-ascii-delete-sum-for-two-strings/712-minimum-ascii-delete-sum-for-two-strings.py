class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1); m = len(s2);
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1,1):
            for j in range(1,m+1,1):
                if(s1[i-1]==s2[j-1]):
                    dp[i][j]=2*ord(s1[i-1])+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        sum=0
        for i in range(n):
            sum+=ord(s1[i]);
        for i in range(m):
            sum+=ord(s2[i])
        return sum-dp[n][m]