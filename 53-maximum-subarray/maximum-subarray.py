class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        n = nums                  
        mv = n[0]
        for v in n:
            sum += v
            mv = max(mv, sum)
            if sum < 0:
                sum = 0
        return mv