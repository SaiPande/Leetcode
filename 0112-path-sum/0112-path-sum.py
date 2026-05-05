# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            stack = [(root, targetSum - root.val)]

            while stack:
                current, remaining =  stack.pop()
                if not current.left and not current.right:
                    if remaining == 0:
                        return True   
                if current.right:
                    stack.append((current.right, remaining - current.right.val))        
                if current.left:
                    stack.append((current.left, remaining - current.left.val))
            

        return False