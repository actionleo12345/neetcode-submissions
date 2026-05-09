class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        
        def become_rotten(r, c):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                grid[r][c] != 1):
                return 0 # we return 0 for the outbound or rotten or no orange, since no fresh orange got rotten
            grid[r][c] = 2
            q.append([r, c])
            return 1 # return -1 for fresh -= 1

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # get how many fresh orange
                    fresh += 1
                if grid[r][c] == 2: # add rotten orange in the q
                    q.append([r, c])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                fresh -= become_rotten(r-1, c)
                fresh -= become_rotten(r+1, c)
                fresh -= become_rotten(r, c-1)
                fresh -= become_rotten(r, c+1)
            time += 1
        
        return time if fresh == 0 else -1