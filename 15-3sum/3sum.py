class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate first element
            left = i + 1
            right = len(nums) - 1
            while left < right:
                add = nums[left] + nums[right] + num
                if add == 0:
                    result.append([nums[left], nums[right], num])
                    left += 1
                    right -= 1
                    # skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif add < 0:
                    left += 1
                else:
                    right -= 1

        return result