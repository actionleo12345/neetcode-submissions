class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = cur_max = nums[0]
        max_product = cur_max

        for num in nums[1:]:
            temp_hold = cur_min
            cur_min = min(num, num * cur_min, num * cur_max)
            cur_max = max(num, num * temp_hold, num * cur_max)
            max_product = max(max_product, cur_max)
        
        return max_product