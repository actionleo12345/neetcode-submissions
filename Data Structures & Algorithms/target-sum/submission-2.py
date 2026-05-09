class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        # initiate a 1 at target=0 and we have 1 way to do it
        dp[0] = 1

        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                new_dp[cur_sum + nums[i]] += count
                new_dp[cur_sum - nums[i]] += count
            dp = new_dp
        return dp[target]