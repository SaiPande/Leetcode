# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        lst = [] 
        while curr:
            lst.append(curr.val)
            curr = curr.next 
        
        lstlen = len(lst)
        if lstlen%2 == 0:
            if lst[0:lstlen//2] == lst[lstlen//2:][::-1]:
                return True
        else: 
            if lst[0:(lstlen//2)] == lst[(lstlen+1)//2:][::-1]:
                return True          
        return False
