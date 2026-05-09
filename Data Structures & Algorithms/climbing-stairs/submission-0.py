class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 1, 1

        for i in range(n):
            tem = l
            l = l+r
            r = tem
        
        return r