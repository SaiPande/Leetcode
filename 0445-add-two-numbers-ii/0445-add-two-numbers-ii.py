# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prevl1 = None
        currentl1 = l1
        prevl2 = None
        currentl2 = l2

        while currentl1:
            temp = currentl1.next
            currentl1.next = prevl1
            prevl1 = currentl1
            currentl1 = temp

        while currentl2:
            temp = currentl2.next
            currentl2.next = prevl2
            prevl2 = currentl2
            currentl2 = temp  

        if not prevl1 and prevl2:
            return prevl2

        if not prevl2 and prevl1:
            return prevl1

        if not prevl1 and not prevl2:
            return None

        dummy = ListNode(0)
        newlist = dummy
        carry = 0

        while prevl1 or prevl2 or carry:
            val1 = prevl1.val if prevl1 else 0
            val2 = prevl2.val if prevl2 else 0

            temp = val1+val2+carry
            if temp > 9: 
               carry = temp//10 
               temp = temp%10 
            else: 
                carry = 0 
            newlist.next = ListNode(temp)    
            newlist = newlist.next

            prevl1 = prevl1.next if prevl1 else None
            prevl2 = prevl2.next if prevl2 else None
        
        prevnew = None
        currentnew = dummy.next          
        while currentnew:
            temp = currentnew.next
            currentnew.next = prevnew
            prevnew = currentnew
            currentnew = temp

        return prevnew   

