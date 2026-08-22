class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in value_to_index:
                return [value_to_index[needed], i]
            value_to_index[num] = i