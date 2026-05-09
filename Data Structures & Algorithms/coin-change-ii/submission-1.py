class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]* (amount+1)
        dp[0] = 1

        for c in range(len(coins)-1, -1, -1):
            next_dp = [0] * (amount+1)
            next_dp[0] = 1
            for a in range(1, amount+1):
                next_dp[a] = dp[a]
                if a - coins[c]>=0:
                    next_dp[a] += next_dp[a - coins[c]]
            dp = next_dp
        
        return dp[-1]