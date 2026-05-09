class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(nums):
                return
            
            # choice01, add
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            
            cur.pop() # need to pop to do the chioce02
            # choice02, not add
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res