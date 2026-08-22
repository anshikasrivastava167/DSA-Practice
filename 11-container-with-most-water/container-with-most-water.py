from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum_area = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            if area > maximum_area:
                maximum_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum_area