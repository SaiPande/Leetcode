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
        while fast and fast.next:
            slowprev = slow
            slow = slow.next
            fast = fast.next.next
        
        slowprev.next = slow.next  
        slow.next = None

        return head  

        # if not head.next: return None

        # slow = head               
        # fast = slow.next.next         starting fast earlier, the slow at the end of while reaches to slowprev

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # slow.next = slow.next.next
        # return head