class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    cur_area = self.dfs(r, c, grid)
                    max_area = max(max_area, cur_area)
        return max_area
    
    def dfs(self, row, col, grid):
        grid[row][col] = 0
        num = 1
        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in directions:
            if (r >= 0 and c >=0
                and r < len(grid) and c < len(grid[0])
                and grid[r][c] == 1):
                num += self.dfs(r, c, grid)
        return num