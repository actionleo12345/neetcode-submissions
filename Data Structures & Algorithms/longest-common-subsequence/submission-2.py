class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for j in range(len(text1) + 1)]

        for row in range(len(text1)-1, -1, -1):
            for col in range(len(text2)-1, -1, -1):
                if text1[row] == text2[col]:
                    # if match, we take the diagonal cell's value + 1
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    # if not match, we take the max value between
                        # the cell value blow us 
                        # and the cell value on our right-hand side
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])

        return dp[0][0]