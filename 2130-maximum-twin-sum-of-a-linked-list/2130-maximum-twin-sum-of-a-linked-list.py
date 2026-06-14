# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:    
        listlength = 0 
        current = head

        while current:
            listlength +=1
            current = current.next

        if listlength%2 == 1:
            return 0   
        else:
            current = head
            count = listlength//2
            prevtomiddle = None
            while current and count > 0:      #finding middle
                prevtomiddle = current
                current = current.next
                count -= 1
            
            prev = None     
            while current:                 # reversing the second hald
                nextnode = current.next
                current.next = prev
                prev = current
                current = nextnode

            if prevtomiddle:              #joing the first and second half
                prevtomiddle.next = prev

            current = head 
            tail = prev
            maxsum = 0
            while tail:                   # finding max sum of twins by iterating from both ends using 2 pointers
                if maxsum < current.val+tail.val:
                    maxsum = current.val+tail.val
                current = current.next
                tail = tail.next
            return maxsum        