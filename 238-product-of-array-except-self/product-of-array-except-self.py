class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums)) # result array
        # if nums is [1, 2, 4, 6]

        prefix = 1 
        # iterate through the array forwards
        # calculate product for everything that comes before
        for i in range(len(nums)):
            result[i] = prefix # 1 # 1 # 2 # 8
            prefix *= nums[i]  # 1 # 2 # 8 # 48
        # result = [1, 1, 2, 8]
        suffix = 1
        # iterate through the array backwards
        # multiply it through backwards
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i] # 6, 24, 48
        return result
        # result = [48, 24, 12, 8]