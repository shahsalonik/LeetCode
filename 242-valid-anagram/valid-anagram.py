class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        for i in range(0, len(t)):
            if s[i] != t[i]:
                return False
        return True
        