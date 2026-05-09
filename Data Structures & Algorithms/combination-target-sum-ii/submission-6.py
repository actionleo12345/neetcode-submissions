class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            #choice01, add
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])

            cur.pop()
            #choice02, not add
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, cur, total)
            return
        
        dfs(0, [], 0)
        return res


        # candidates.sort()
        # res = []

        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return
        #     if total > target or i >= len(candidates):
        #         return
            
        #     # choice01, add
        #     cur.append(candidates[i])
        #     dfs(i + 1, cur, total + candidates[i])
        #     cur.pop() # need to pop (remove) the number since we are gonna go through choice02, not add

        #     # choice02, not add
        #     while  i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
        #         i += 1
        #     dfs(i+1, cur, total)
        
        # dfs(0, [], 0)
        # return res
        
        