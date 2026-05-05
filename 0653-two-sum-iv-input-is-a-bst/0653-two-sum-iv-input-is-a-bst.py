# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return False    
        else:
            outputlist = []
            stack = [root]
            flag = False
            while stack:            
                current = stack.pop()
                if current.left:
                    stack.append(current.left)    
                if current.right:
                    stack.append(current.right)  
                if (k-current.val) in outputlist:
                    return True
                outputlist.append(current.val)            
            return False           
