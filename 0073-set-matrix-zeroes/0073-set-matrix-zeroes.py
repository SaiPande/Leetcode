class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst = []
        flagrowzero = False
        for i in range(len(matrix)):
            if 0 in matrix[i]:
               lst.extend(idx for idx, val in enumerate(matrix[i]) if val == 0)
               flagrowzero = True
            if flagrowzero == True:
                matrix[i] = [0] * len(matrix[i])
                flagrowzero = False

        for row in matrix:
            for col_index in lst:
                row[col_index] = 0