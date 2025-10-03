class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targ_map = {}

        for i, val in enumerate(nums):
            need = target - val
            if need in targ_map:
                return [i, targ_map[need]]

            targ_map[val] = i
        return [-1, -1]