class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        length = right - left
        curr_area = min(height[left], height[right]) * length

        # this loop condition can't be length > 0
        # this is bc it's the pointers that are changing
        # not just the length (if the pointers change, the length does too)
        while left < right:
            length = right - left
            total = min(height[left], height[right]) * length
            if total > curr_area:
                curr_area = total
            elif height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        return curr_area