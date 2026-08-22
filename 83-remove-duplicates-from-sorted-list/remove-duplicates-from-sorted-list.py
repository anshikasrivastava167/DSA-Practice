# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        while t:
            if t.next != None and t.val == t.next.val:
                temp = t.next
                t.next = temp.next
                temp.next = None
            else:
                t = t.next
        return head