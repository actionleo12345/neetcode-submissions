class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        visited_pac, visited_atl = set(), set()

        def dfs(r, c, visited, pre_height):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                (r, c) in visited or
                pre_height > heights[r][c]):
                return
            # add current one in the visited set if it passed the above check
            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])

        # first and last rows touch Pacific
        for c in range(cols):
            dfs(0, c, visited_pac, heights[0][c])
            dfs(rows - 1, c, visited_atl, heights[rows - 1][c])
        
        # first and last cols toch Atlantic
        for r in range(rows):
            dfs(r, 0, visited_pac, heights[r][0])
            dfs(r, cols - 1, visited_atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited_pac and (r,c) in visited_atl:
                    res.append([r, c])
        
        return res
