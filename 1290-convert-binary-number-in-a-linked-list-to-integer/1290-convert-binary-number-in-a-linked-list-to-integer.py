# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        count = 0
        n = 0
        while current:
            n += 1
            current = current.next
        current = head    
        while current: 
            count += (current.val)*(2**(n-1))
            current = current.next  
            n -= 1  
        return count    
