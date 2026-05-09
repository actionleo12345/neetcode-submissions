class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, window = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(window[:])
                return

            # choice01, not add
            backtrack(i+1)

            # choice02, add
            window.append(nums[i])
            backtrack(i+1)
            window.pop() # we need to pop it so to include all cases
            return

        backtrack(0)
        return res