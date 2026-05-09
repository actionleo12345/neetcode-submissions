class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        for i in range(amount + 1):
            dp.append(float('inf'))

        dp[0] = 0

        for ind_amt in range(1, amount + 1):
            for coin in coins:
                if coin <= ind_amt:
                    dp[ind_amt] = min(dp[ind_amt], dp[ind_amt - coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
