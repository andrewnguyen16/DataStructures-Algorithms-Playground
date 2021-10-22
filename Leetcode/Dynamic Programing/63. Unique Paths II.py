class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        check = False
        for i in range(0, m):
            if check or obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                check = True
            else:
                dp[i][0] = 1
                # print(dp[1][1])

        check = False
        for j in range(0, n):
            if check or obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                check = True
            else:
                dp[0][j] = 1

        i = j = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
