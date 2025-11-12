class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targMap = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in targMap:
                return [targMap[need], i]
            targMap[num] = i