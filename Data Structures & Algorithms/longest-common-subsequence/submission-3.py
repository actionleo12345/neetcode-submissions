class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1)+1, len(text2)+1

        dp = [[0]*cols for _ in range(rows)]

        for r in range(1, rows):
            for c in range(1, cols):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return dp[-1][-1]