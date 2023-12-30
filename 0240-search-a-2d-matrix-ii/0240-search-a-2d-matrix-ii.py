class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        for i in range(rows):
            a = matrix[i][0]
            b = matrix[i][cols - 1]
            if a <= target <= b:
                left, right = 0, cols - 1
                while left <= right:
                    mid = (left + right) // 2
                    mid_value = matrix[i][mid]
                    if mid_value == target:
                        return True
                    elif mid_value < target:
                        left = mid + 1
                    else:
                         right = mid - 1
        return False


                    
                    
                
        
        