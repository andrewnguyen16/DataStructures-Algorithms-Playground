class Solution:
    def coinChange(self, coins, amount):
        row = len(coins) + 1
        col = amount + 1

        dp = [[0 for x in range(col)] for y in range(row)]

        for m in range(0, row):
            dp[m][0] = 0
        for n in range(1, col):
            dp[0][n] = 1e5

        for i in range(1, row):
            for j in range(1, col):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])

        return dp[row - 1][col - 1] if dp[row - 1][col - 1] < 1e5 else -1
