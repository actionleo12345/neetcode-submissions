class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(cur, start, target):
            if target == 0:
                res.append(cur.copy())
                return
            
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break
                dfs(cur + [nums[i]], i, target - nums[i])
        
        dfs([], 0, target)
        return res