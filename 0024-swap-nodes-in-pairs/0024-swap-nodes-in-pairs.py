# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if head and not head.next:
            return head

        prev = None
        current = head
        new_head = head.next
        while current and current.next:
            temp = current.next
            current.next= temp.next
            temp.next = current
            
            if prev:
                prev.next = temp

            prev = current
            current = current.next             

        return new_head    