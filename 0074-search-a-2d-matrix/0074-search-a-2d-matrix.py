class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        # Traverse the rows first and then columns
        for i in range(row):
            if matrix[i][0] <= target <= matrix[i][col-1]:
                # Binary search within the current row
                left, right = 0, col - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                continue

        return False
