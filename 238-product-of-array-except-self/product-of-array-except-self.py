class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        total_product = 1
        total_product_no_zero = 1
        zero_count = 0

        for num in nums:
            total_product *= num
            if num != 0:
                total_product_no_zero *= num
            if num == 0:
                zero_count += 1

        for i in range(len(nums)):
            if nums[i] == 0 and zero_count <= 1:
                result.append(total_product_no_zero)
            elif nums[i] == 0 and zero_count > 1:
                result.append(total_product)
            else:
                result.append(int(total_product / nums[i]))

        return result