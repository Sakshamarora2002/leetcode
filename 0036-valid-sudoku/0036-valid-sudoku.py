class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    if (i, element) in seen or (element, j) in seen or (i // 3, j // 3, element) in seen:
                        return False
                    seen.add((i, element))
                    seen.add((element, j))
                    seen.add((i // 3, j // 3, element))
        
        return True