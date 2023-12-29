from typing import List
import numpy as np

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = np.zeros((n, n), dtype=int)
        num = 1
        top, bottom, left, right = 0, n-1, 0, n-1

        while num <= n*n:
            # Traverse from left to right
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Traverse from right to left
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # Traverse from bottom to top
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix.tolist()


# Usage example
n = 4  # Size of the spiral matrix

solution = Solution()
spiral_matrix = solution.generateMatrix(n)

for row in spiral_matrix:
    print(row)
