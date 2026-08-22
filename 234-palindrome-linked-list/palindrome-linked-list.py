# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s1 = []
        sp = fp = head

        while fp and fp.next:
            s1.append(sp.val)
            sp = sp.next
            fp = fp.next.next

        if fp:
            sp = sp.next

        while sp:
            if sp.val != s1[-1]:
                return False
            s1.pop()
            sp = sp.next

        if len(s1) == 0:
            return True
        return False