class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(r, c, grid)
                    n_islands += 1
        
        return n_islands

    def dfs(self, row, col, grid):
        grid[row][col] = "0"
        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in directions:
            if (c >=0 and r >=0 and 
               r < len(grid) and c < len(grid[0])
               and grid[r][c] == "1"):
                self.dfs(r, c, grid)