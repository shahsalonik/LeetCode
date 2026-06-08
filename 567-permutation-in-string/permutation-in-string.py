class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import Counter

        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if target == window:
            return True

        for i in range(len(s1), len(s2)):
            entering = i
            leaving = i - len(s1)

            window[s2[entering]] += 1
            window[s2[leaving]] -= 1

            if window[s2[leaving]] == 0:
                del window[s2[leaving]]

            if target == window:
                return True

        return False