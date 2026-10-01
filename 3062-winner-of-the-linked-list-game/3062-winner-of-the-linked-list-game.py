# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        if not head:
            return 'Tie'
        
        prev = head 
        current = head.next
        odd = 0
        even = 0
        while prev and current:
            if prev.val > current.val:
                even+=1
            elif prev.val < current.val:
                odd+=1
            
            if current.next and current.next.next:
                prev = current.next
                current = current.next.next
            else:
                break    

        if even>odd:
            return "Even"
        elif even<odd:
            return "Odd"
        else:
            return "Tie"                
