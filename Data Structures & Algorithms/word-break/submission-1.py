class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        trues = [0] # create a new list that only contains indices that value = True
        for right in range(n):
            for left in trues:
                if s[left:right] in wordDict:
                    dp[right] = True
                    trues.append(right)
                    break
        
        return dp[-1]
