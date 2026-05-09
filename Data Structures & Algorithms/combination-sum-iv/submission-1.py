class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {0:1}

        def dfs(total):
            if total in memo:
                return memo[total]
            
            res = 0
            for n in nums:
                if n > total:
                    break
                res += dfs(total - n)
            memo[total] = res
            return res
        
        return dfs(target)