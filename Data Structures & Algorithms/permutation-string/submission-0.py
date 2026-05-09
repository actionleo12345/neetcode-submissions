class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if (s1Count[i] == s2Count[i]) else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # we slide the window to next index
            new_index = ord(s2[r]) - ord('a')
            s2Count[new_index] += 1
            if s1Count[new_index] == s2Count[new_index]:
                matches += 1
            elif s1Count[new_index] + 1 == s2Count[new_index]:
                matches -= 1

            # since we slide the window to next index, we remove the old(left) index value
            old_index = ord(s2[l]) - ord('a')
            s2Count[old_index] -= 1
            if s1Count[old_index] == s2Count[old_index]:
                matches += 1
            elif s1Count[old_index] - 1 == s2Count[old_index]:
                matches -= 1
            l += 1
        
        return matches == 26



