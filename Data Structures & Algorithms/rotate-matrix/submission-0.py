class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            # we rotate outer layer then layer-by-layer to internal layer
            for i in range(r - l):
                top, bottom = l, r
                
                # save top left number in temp
                topleft = matrix[top][l + i]
                
                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # put temp save topleft to top right
                matrix[top + i][r] = topleft
            l += 1
            r -= 1