class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_len = len(t)
        s_len = len(s)
        if t_len < s_len:
            return False
        if s == "":
            return True
        
        ind = 0
        for c in t:
            print(ind)
            print(s[ind], " ", c)
            if s[ind] == c:
                ind += 1
            if ind >= s_len:
                return True
        return False
        