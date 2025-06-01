class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        for i in s:
            count = t_count.get(i)
            if count is None or count != s_count.get(i):
                return False
        return True
        