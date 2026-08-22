# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = t = None
        temp = None

        while head:
            if head.next and head.val == head.next.val:
                temp = head
                head = head.next
            else:
                if temp and head.val == temp.val:
                    temp = head
                    head = head.next
                else:
                    if h is None:
                        tm = temp = head
                        head = head.next
                        tm.next = None
                        h = t = tm
                    else:
                        tm = head
                        head = head.next
                        tm.next = None
                        t.next = tm
                        t = tm

        return h