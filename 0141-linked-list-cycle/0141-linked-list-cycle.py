# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #2 pointer - slow and fast 
        #hare and tortoise 

        fast = head 

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if fast == head:
                return True
        return False    