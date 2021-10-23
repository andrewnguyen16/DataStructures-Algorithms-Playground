class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False

        findSum = int(total / 2)
        column = findSum + 1
        row = len(nums) + 1
        dp = [[False for x in range(column)] for y in range(row)]

        for i in range(0, row):
            dp[i][0] = True

        for i in range(1, row):
            for j in range(1, column):
                if j == 0:
                    continue
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                elif nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[row - 1][column - 1]
