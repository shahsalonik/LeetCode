class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left, right = 0, 0
        max_len = 0

        while right < len(s):
            if s[right] not in charset:
                charset.add(s[right])
                max_len = max(max_len, len(charset))
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])
            right += 1

        return max_len