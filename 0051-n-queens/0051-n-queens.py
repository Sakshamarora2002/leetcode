class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col, n):
            for i in range(col):
                if board[row][i] == 1:
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            return True
        
        def solve_n_queens(board, col, n, solutions):
            if col >= n:
                queens = []
                for i in range(n):
                    row = ""
                    for j in range(n):
                        if board[i][j] == 1:
                            row += "Q"
                        else:
                            row += "."
                    queens.append(row)
                solutions.append(queens)
                return
            
            for i in range(n):
                if is_safe(board, i, col, n):
                    board[i][col] = 1
                    solve_n_queens(board, col+1, n, solutions)
                    board[i][col] = 0
        
        board = [[0] * n for _ in range(n)]
        solutions = []
        solve_n_queens(board, 0, n, solutions)
        
        return solutions
