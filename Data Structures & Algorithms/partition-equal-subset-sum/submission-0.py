class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums) // 2
        for i in range(len(nums)):
            dp_temp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                
                dp_temp.add(t + nums[i])
                dp_temp.add(t)
            dp = dp_temp
        
        return False
        