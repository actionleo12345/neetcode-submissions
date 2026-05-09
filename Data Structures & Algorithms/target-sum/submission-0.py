class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums)+1)]

        # initiate a 1 at target=0 and we have 1 way to do it
        dp[0][0] = 1

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum + nums[i]] += count
                dp[i+1][cur_sum - nums[i]] += count
        
        return dp[len(nums)][target]
