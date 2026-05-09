class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # top row from left to right
            for c in range(left, right):
                res.append(matrix[top][c])
            top += 1
            
            # rightmost column top to bottom
            for r in range(top, bottom):
                res.append(matrix[r][right-1])
            right -= 1

            # reason: we might converge rows or columns, but if let's say rows are converged, but there are still some columns we can iterate, which is not what we want
            if not (left < right and top < bottom):
                break

            # bottom row from right to left
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][c])
            bottom -= 1

            # leftmost column bottom to top
            for r in range(bottom -1, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
        
        return res
