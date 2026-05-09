class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_0 = False

        # loop to check each cell
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # set the first row's corresponding col as 0
                    matrix[0][c] = 0
                    
                    # if it's not first row then we set the left most cell of that row as 0 to indicate this row will become 0
                    if r > 0:
                        matrix[r][0] = 0
                    # if it's first row, then we need that left most cell for checking if the corresponding column needs to be 0 or not. so we use this extra variable to hold if the first row needs to be 0 or not
                    else:
                        first_row_0 = True

        # other than first row and first column, if we see 0 we convert that whole row and column to 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # check if we can convert first column to 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # check if we can covert first row to 0
        if first_row_0:
            for c in range(cols):
                matrix[0][c] = 0