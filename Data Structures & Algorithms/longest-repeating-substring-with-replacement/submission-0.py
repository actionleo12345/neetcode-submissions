class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_len = 0
        most_freq = 0
        count = {}
        while right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            most_freq = max(most_freq, count[s[right]])
            if most_freq + k < right - left + 1:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len