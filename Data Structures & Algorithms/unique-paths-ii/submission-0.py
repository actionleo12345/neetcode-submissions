class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0]*m
        dp[m-1] = 1

        for r in reversed(range(n)):
            for c in reversed(range(m)):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < m:
                    dp[c] = dp[c] + dp[c+1]
                # else:
                #     dp[c]
        
        return dp[0]