class Solution:
    def exist(self, board, word):
        rows = len(board)
        if rows == 0:
            return False
        cols = len(board[0])
        
        def dfs(i, j, k):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            temp = board[i][j]
            board[i][j] = "#" 
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if dfs(new_i, new_j, k + 1):
                    return True
            
            board[i][j] = temp 
            return False
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False

        