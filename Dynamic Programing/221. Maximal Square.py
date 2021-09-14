class Solution:
    def maximalSquare(self, matrix):
        if len(matrix) < 1:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        max_size = 0
        for i in range(0, row):
            for j in range(0, col):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] != 0 and i > 0 and j > 0:
                    matrix[i][j] = (
                        min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
                        + 1
                    )
                max_size = max(max_size, matrix[i][j])
        return max_size * max_size
