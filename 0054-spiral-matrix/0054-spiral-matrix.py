from typing import List
import numpy as np

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = np.array(matrix) 
        spiral_order = []
        while matrix.size > 0:
            # Traverse top row
            spiral_order.extend(matrix[0])
            # Remove the top row
            matrix = matrix[1:]
            if matrix.size == 0:
                break
            # Traverse rightmost column
            spiral_order.extend(matrix[:, -1])
            # Remove the rightmost column
            matrix = matrix[:, :-1]
            if matrix.size == 0:
                break
            # Traverse bottom row (in reverse order)
            spiral_order.extend(matrix[-1][::-1])
            # Remove the bottom row
            matrix = matrix[:-1]
            if matrix.size == 0:
                break
            # Traverse leftmost column (in reverse order)
            spiral_order.extend(matrix[:, 0][::-1])
            # Remove the leftmost column
            matrix = matrix[:, 1:]
        return spiral_order
