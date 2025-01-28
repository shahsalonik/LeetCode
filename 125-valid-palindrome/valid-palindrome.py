class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(ch for ch in s.lower() if ch.isalnum())
        for i in range(0, len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

        