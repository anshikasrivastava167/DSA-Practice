# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        count = 0 
        temp = head
        while temp:
            count += 1
            temp = temp.next
        re = k % count
        if re == 0:
            return head
        temp = head
        index = count - re - 1
        while index:
            index -= 1
            temp = temp.next
        tm = temp.next
        temp.next = None
        temp = tm
        while temp.next:
            temp = temp.next
        temp.next = head
        return tm