class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hp = {}
        size = -(len(nums2))
        index = -1
        while(size <= index):
            data = nums2[index]
            while stack:
                if stack[-1] > data:
                    hp[data] = stack[-1]
                    break
                else:
                    stack.pop()
            if not stack: 
                hp[data] = -1
            stack.append(data)
            index -= 1

        ans = []
        for value in nums1:
            ans.append(hp[value])
        return ans