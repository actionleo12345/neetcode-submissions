class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        start, end = 0 , 0
        cur_sum = 0

        for end in range(len(nums)):
            cur_sum += nums[end]
            while cur_sum >= target:
                min_size = min(min_size, end - start + 1)
                cur_sum -= nums[start]
                start += 1

        return min_size if min_size != float('inf') else 0