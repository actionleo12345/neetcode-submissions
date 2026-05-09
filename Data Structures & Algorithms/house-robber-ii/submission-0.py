class Solution:
    def helper(self, nums):
        for i in range(1, len(nums)):
            if i == 1:
                nums[i] = max(nums[i], nums[i-1])
            else:
                nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        return nums[-1]
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))