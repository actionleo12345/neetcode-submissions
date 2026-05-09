class Solution:
    def helper(self, coins, amt):
        if amt in self.memo:
            return self.memo[amt]

        min_coin_need = float('inf')
        for coin in coins:
            if coin <= amt:
                coin_need = self.helper(coins, amt-coin)
                min_coin_need = min(min_coin_need, coin_need)
        if min_coin_need != float('inf'):
            min_coin_need += 1
        
        self.memo[amt] = min_coin_need
        return min_coin_need



    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        self.memo[0] = 0

        for coin in coins:
            if coin <= amount:
                self.memo[coin] = 1
        
        coins.sort()

        res = self.helper(coins, amount)
        return res if res != float('inf') else -1
