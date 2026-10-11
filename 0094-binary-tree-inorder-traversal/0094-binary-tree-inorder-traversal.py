# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        elif root.left == None and root.right == None:
            return [root.val]   
        else:    
            output = []
            self.inorder(root, output)
            return output

    def inorder(self, root, output):
        if root is not None: 
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)    