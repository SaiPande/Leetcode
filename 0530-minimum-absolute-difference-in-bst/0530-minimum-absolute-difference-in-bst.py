# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:    
            listofnumbers = []
            stack = []
            #stack.append(root)
            current = root
            while stack or current:
                while current: 
                    stack.append(current)
                    current = current.left                           
                current = stack.pop()   
                listofnumbers.append(current.val)     
                current = current.right   
        minval = 999999
        for i in range(len(listofnumbers)-1):
            if abs(listofnumbers[i+1]-listofnumbers[i]) < minval:
                minval = abs(listofnumbers[i+1]-listofnumbers[i])
        return minval        

