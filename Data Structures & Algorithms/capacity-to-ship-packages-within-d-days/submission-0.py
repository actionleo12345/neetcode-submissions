class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        min_cap = r

        def can_ship(cap):
            need_days, cur_cap = 1, cap
            for w in weights:
                if cur_cap - w < 0:
                    need_days += 1
                    cur_cap = cap
                cur_cap -= w
            return need_days <= days


        while l <= r:
            mid_cap = (l+r) // 2
            if can_ship(mid_cap):
                min_cap = min(min_cap, mid_cap)
                r = mid_cap - 1
            else:
                l = mid_cap + 1
        
        return min_cap