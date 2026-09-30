# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root or not root.left:
            return root

        else:
            current = root 
            prev = None
            prev_right = None
            while current:
                rt = current.right   #z
                lt = current.left    #y

                
                current.left = prev_right  #none
                current.right = prev

                prev_right = rt
                prev = current
                current = lt   

        return prev            




