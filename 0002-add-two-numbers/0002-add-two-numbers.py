# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and l2:
            return l2

        if not l2 and l1:
            return l1

        if not l1 and not l2:
            return None    

        dummy = ListNode(0)
        newlist = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            temp = val1+val2+carry
            if temp > 9: 
               carry = temp//10 
               temp = temp%10 
            else: 
                carry = 0 
            newlist.next = ListNode(temp)    
            newlist = newlist.next
            print(newlist.val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next    



