class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, preVal):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                matrix[r][c] <= preVal):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            cur_max = 1
            cur_max = max(cur_max, 1 + dfs(r-1, c, matrix[r][c]))
            cur_max = max(cur_max, 1 + dfs(r+1, c, matrix[r][c]))
            cur_max = max(cur_max, 1 + dfs(r, c-1, matrix[r][c]))
            cur_max = max(cur_max, 1 + dfs(r, c+1, matrix[r][c]))
            
            dp[(r, c)] = cur_max
            return cur_max

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)

        return max(dp.values())