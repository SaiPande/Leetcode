# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            current = current.next
            count +=1

        print(count)

        if n == 1 and count == 1:
            return None  

        if count < n:
            return head

        elif count == n:
            return head.next
    
        
        else:
            deleteval = count - n +1
            count2 = 0
            
            dummy = ListNode(0)
            dummy.next = head

            current = dummy
            prev = None
            
            while current:
                if count2 == deleteval:
                    print(count2)
                    print(prev.val)
                    print(current.val)
                    prev.next = current.next
                else:    
                    prev = current
                current = current.next
                count2 +=1
        return dummy.next  

