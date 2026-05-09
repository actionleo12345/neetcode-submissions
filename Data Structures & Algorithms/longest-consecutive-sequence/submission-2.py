class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0

        for n in nums:
            if (n-1) not in numSet:
                cur_len = 1
                while (n + cur_len) in numSet:
                    cur_len += 1
                
                max_len = max(max_len, cur_len)
            
        return max_len