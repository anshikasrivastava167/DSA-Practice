from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        leftmax = [0] * size
        rightmax = [0] * size

        leftmax[0] = height[0]
        rightmax[size - 1] = height[size - 1]

        for i in range(1, size):
            leftmax[i] = max(leftmax[i - 1], height[i])

        for i in range(size - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])

        ans = 0
        for i in range(size):
           ans += min(leftmax[i], rightmax[i]) - height[i]

        return ans