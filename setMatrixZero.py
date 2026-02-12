class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # 1. Check if the first row or first col need to be zeroed later
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True

        # 2. Use first row/col as markers for the rest of the matrix
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 3. Use those markers to set zeros
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 4. Finally, handle the first row and first col themselves
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0
