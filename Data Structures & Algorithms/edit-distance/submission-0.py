class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n_cols = len(word1) + 1
        n_rows = len(word2) + 1

        dp = [[0 for c in range(n_cols)] for r in range(n_rows)]

        # fill up first row 
        for c in range(n_cols):
            dp[0][c] = c

        # fill up first column
        for r in range(n_rows):
            dp[r][0] = r
        

        for r in range(1, n_rows):
            for c in range(1, n_cols):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
        
        return dp[r][c]