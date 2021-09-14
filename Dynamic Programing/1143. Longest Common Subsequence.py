class Solution:
    def longestCommonSubsequence(self, text1, text2):
        l1 = len(text1) + 1
        l2 = len(text2) + 1
        maxLength = 0
        dp = [[0 for x in range(l2)] for y in range(l1)]
        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if dp[i][j] > maxLength:
                    maxLength = dp[i][j]
        return maxLength
