class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)

        if len(freq_s.keys()) != len(freq_t.keys()):
            return False

        for key, val in freq_s.items():
            if not freq_t[key]: 
                return False
            if freq_t[key] != val:
                return False
        
        return True