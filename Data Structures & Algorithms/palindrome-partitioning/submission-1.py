class Solution:
    def ispalin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
            
            for j in range(i, len(s)):
                if self.ispalin(s, i, j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop() # pop out the element we just added, ensure a clean new start
        
        dfs(0)
        return res