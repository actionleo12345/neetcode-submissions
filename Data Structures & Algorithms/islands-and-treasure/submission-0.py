class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])

        def add_to_q(r, c):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                (r,c) in visited or
                grid[r][c] == -1):
                return # either outbound or already visited or it's an obstacle
            q.append([r, c])
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_to_q(r-1, c)
                add_to_q(r+1, c)
                add_to_q(r, c-1)
                add_to_q(r, c+1)
            dist += 1
        