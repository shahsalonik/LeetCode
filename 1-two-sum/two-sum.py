class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in index_dict.keys():
                return sorted([i, index_dict[res]])
            else:
                index_dict[nums[i]] = i

        return [-1, -1]