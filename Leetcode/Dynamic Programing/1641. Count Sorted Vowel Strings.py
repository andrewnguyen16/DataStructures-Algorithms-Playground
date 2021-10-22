class Solution:
    def countVowelStrings(self, n):
        dp = [[0 for x in range(5)] for y in range(n)]
        dp[0][0] = 1
        dp[0][1] = 2
        dp[0][2] = 3
        dp[0][3] = 4
        dp[0][4] = 5
        if n == 1:
            return 5
        for i in range(1, n):
            for j in range(0, 5):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[n - 1][4]
