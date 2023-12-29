class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        import numpy as np
        arr = np.array(matrix)
        #transpose of the matrix .T
        arr = arr.T
        #flip the matrix
        arr = np.flip(arr, axis=1)
        matrix[:] = arr.tolist()