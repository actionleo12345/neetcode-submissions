class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            dic[n] = 1 + dic.get(n, 0)

        for value, count in dic.items():
            freq[count].append(value)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for e in freq[i]:
                res.append(e)
            
            if len(res) == k:
                return res

        
