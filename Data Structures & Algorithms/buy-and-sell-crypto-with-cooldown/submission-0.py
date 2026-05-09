class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        for i in range(n-1, -1, -1):
            # boolan in index: True=1/False=0
            for can_buy in [True, False]:
                if can_buy:
                    #choice01, we buy the stock. 
                        #check tomorrow(i+1)'s "cannot buy tomrrow" case(can_buy=False)
                        #since choice01 means we "buy the stock today" case
                    amt_after_buy = dp[i+1][False] - prices[i] if i+1<n else -prices[i]
                    #choice02, we cooldown, meaning we do nothing.
                        # since today's status is can buy (can_buy=True), meaning we do not hold any stock. 
                        # and then tomorrow's status will be can buy status as well, based on that status, what's the max value we can get.
                    amt_after_cooldown = dp[i+1][True] if i+1<n else 0
                    # based on today's can buy status (can_buy=True), what's max value that we aggregate tomorrow's value(based on today's "can buy" status)
                    dp[i][True] = max(amt_after_buy, amt_after_cooldown)
                
                # can_buy=False, meaning we hold a sotck, we cannot buy but we can sell the holding stock
                else:
                    #choice01, we sell the holding stock
                        # since we sell the stock today, two days after, the status will be can_buy=True. We need to check that day (two day after) 's max value based on that day(two day after) "can buy"
                        # Why not check tomrrow? since today we sell so tomorrow must be cooldown. so we skip tomorrow
                    amt_after_sell = dp[i+2][True] + prices[i] if i+2<n else prices[i]
                    #choice02, we cooldown, meaning we do nothing.
                        # since today's status is cannot buy (can_buy=False), meaning we do hold any stock. 
                        # and then tomorrow's status will be cannot buy status as well(since we do nothing today, and the stock is still in our hand), based on that status(tomorrow still cannot buy status), what's the max value we can get.
                    amt_after_cooldown = dp[i+1][False] if i+1<n else 0
                    #  based on today's cannot buy status (can_buy=False), what's max value that we aggregate tomorrow's value(based on today's "cannot buy" status)
                    dp[i][False] = max(amt_after_sell, amt_after_cooldown)
        
        return dp[0][1]