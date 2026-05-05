# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # l = 0
        # current = head
        # while current:
        #     current = current.next
        #     l+=1
        
        # mid = l//2  
        # current = head
        # while mid > 0:
        #     current = current.next
        #     mid -= 1
        # return current 

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow            