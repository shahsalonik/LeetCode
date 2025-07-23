class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = {}
        for i in nums:
            if i in duplicate_dict.keys():
                return True
            else:
                duplicate_dict[i] = 1
        return False