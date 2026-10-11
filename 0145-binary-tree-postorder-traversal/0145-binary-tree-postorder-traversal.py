# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []

        elif root.left == None and root.right == None:
            return [root.val]

        else:
            output = []
            self.postorder(root, output)
            return output

    def postorder(self, root, output):
        if root is not None:
            self.postorder(root.left, output)
            self.postorder(root.right,output)
            output.append(root.val)        
