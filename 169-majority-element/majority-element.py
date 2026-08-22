class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        n = len(nums)

        for v in nums:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

        for key in d:
            if d[key] > (n // 2):
                return key