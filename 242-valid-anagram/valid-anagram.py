class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc=collections.Counter(s)
        tc=collections.Counter(t)
        if len(s)!=len(t):
            return False
        for k,v in sc.items():
            if tc[k]!=v:
                return False
        return True