# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 0
        else:
            sum = 0
            flag = 0
            stack = [(root,flag)]
            while stack:
                current,flag = stack.pop()
                
                if current.right:
                    stack.append((current.right, 0))
                if current.left:
                    stack.append((current.left, 1)) 
                if not current.left and not current.right and flag == 1:
                    sum += current.val
        return sum                          