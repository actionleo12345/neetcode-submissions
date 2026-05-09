class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = math.ceil(sum(piles) / h)
        high = max(piles)

        while low <= high:
            m = low + ((high-low)//2)
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
                if hours > h:
                    break
            
            if hours <= h:
                high = m -1
            else:
                low = m + 1
        
        return low
            
