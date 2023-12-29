class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def count_live_neighbors(row, col):
            count = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            for dy, dx in directions:
                new_row, new_col = row + dx, col + dy
                
                if 0 <= new_row < m and 0 <= new_col < n and abs(board[new_row][new_col]) == 1:
                    count += 1
            
            return count
        
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                current_state = board[i][j]
                
                if current_state == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1
                elif current_state == 0 and live_neighbors == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
