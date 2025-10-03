class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            need = target - nums[i]
            if need in nums and nums.index(need) != i:
                result.append(i)
                result.append(nums.index(need))
                break
        
        return sorted(result)