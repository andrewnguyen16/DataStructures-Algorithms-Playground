class Solution:
    def solveSudoku(self, board):
        def isValid(board, row, col, num):
            for i in range(0, 9):
                if board[row][i] == num:
                    return False  # check row
                if board[i][col] == num:
                    return False  # check column
            # Check sub board (3 x 3)
            row = (row // 3) * 3
            col = (col // 3) * 3
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def isEmpty(board):
            for i in range(0, 9):
                for j in range(0, 9):
                    if board[i][j] == ".":
                        return (i, j)
            return -1

        while isEmpty(board) != -1:
            m, n = isEmpty(board)
            for num in "123456789":
                if isValid(board, m, n, num):
                    board[m][n] = num
                    if self.solveSudoku(board):
                        return True
                    else:
                        board[m][n] = "."
            return False

        return True
