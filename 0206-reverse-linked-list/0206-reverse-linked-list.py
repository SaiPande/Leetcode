# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head and not head.next:
            return head

        prev = head
        
        current = prev.next
        prev.next = None
        future = None
        while current:
            future = current.next
            current.next = prev
            prev = current
            current = future                     

        return prev        
