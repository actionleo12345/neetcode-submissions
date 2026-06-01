class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            less, equal, greater, pivot = l, l, r, nums[r]
            while equal <= greater: 
                while equal <= greater and nums[equal] < pivot:
                    nums[less], nums[equal] = nums[equal], nums[less]
                    less += 1
                    equal += 1
                while equal <= greater and nums[equal] == pivot:
                    equal += 1
                while equal <= greater and nums[equal] > pivot:
                    nums[greater], nums[equal] = nums[equal], nums[greater]
                    greater -= 1

            if k > greater:
                return quickSelect(greater + 1, r)
            elif k < less:
                return quickSelect(l, less - 1)
            else:
                return nums[greater]

        return quickSelect(0, len(nums) - 1)