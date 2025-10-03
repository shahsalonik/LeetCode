class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targ_map = {} # map for num to index

        for i, val in enumerate(nums):
            need = target - val
            if need in targ_map: # ensures you don't visit the same index
                return [i, targ_map[need]] # will return in inverted order
            targ_map[val] = i

        return [-1, -1] # should never reach