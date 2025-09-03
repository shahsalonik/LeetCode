class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        second = len(height) - 1
        max_volume = 0
        # volume is w x h of lower bar
        while first < second:
            width = second - first
            heights = min(height[first], height[second])
            volume = width * heights
            if volume > max_volume:
                max_volume = volume
            if height[first] < height[second]:
                first += 1
            else:
                second -= 1
        return max_volume