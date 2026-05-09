class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}

        for tar in range(1, target + 1):
            dp[tar] = 0
            for n in nums:
                dp[tar] += dp.get(tar - n, 0)
        
        return dp[target]