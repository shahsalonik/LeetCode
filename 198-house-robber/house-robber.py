class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob2, rob1 + num)
            rob1 = rob2
            rob2 = temp
        return rob2
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i], dp[i - 1], nums[i] + dp[i - 2])
        
        # return dp[-1]