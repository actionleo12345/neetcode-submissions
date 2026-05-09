class Solution:
    def helper(self, nums):
        pre_pre_house, pre_house = 0, 0
        for i in range(len(nums)):
            cur_house = max(nums[i] + pre_pre_house, pre_house)
            pre_pre_house = pre_house
            pre_house = cur_house
        return cur_house

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))