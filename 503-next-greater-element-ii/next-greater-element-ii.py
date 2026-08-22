class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        size = len(nums)
        ans = [0] * size

        for index in range(size *2-1, -1, -1):
            data = nums[index % size]
            while stack:
                if stack[-1] > data:
                    ans[index % size] = stack [-1]
                    break
                else:
                    stack.pop()
            if not stack:
                ans [index % size] = -1
            stack.append(data)
        return ans