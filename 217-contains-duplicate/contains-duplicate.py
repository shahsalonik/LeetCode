class Solution:
    from collections import Counter
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for key, val in freq.items():
            if val > 1:
                return True

        return False