# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = head 
        fast = head
        length = 0
        while fast and fast.next:
            slowprev = slow
            slow = slow.next
            fast = fast.next.next
            length += 1
        
        slowprev.next = slow.next  
        slow.next = None

        return head  