class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        l = 0
        s1_count = Counter(list(s1))

        for idx in range(len(s2) - len(s1) + 1):
            if s1_count == Counter(list(s2[idx:(idx + len(s1))])):
                return True
        
        return False