class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        # target = math.ceil(stone_sum/2)
        target = (stone_sum + 1) // 2
        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stone_sum-total))
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i+1, total), # means we don't pick current stone
                                 dfs(i+1, total + stones[i])) # means we pick current stone
            
            return dp[(i, total)]

        return dfs(0, 0)