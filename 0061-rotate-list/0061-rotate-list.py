# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head     
    
        current = head
        length = 1

        # found length and later made it circular
        while current.next: 
            current = current.next 
            length += 1
        current.next = head

        k = k % length
        steps = length - k - 1

        current = head 
        for _ in range(steps):        
            current = current.next

        new_head = current.next
        current.next = None

        return new_head
            
