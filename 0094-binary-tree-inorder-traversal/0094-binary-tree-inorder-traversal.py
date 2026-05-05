# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            result = []
            self.recurr(root, result)
            return result

    def recurr(self, root, result):
        if root is not None:
            self.recurr(root.left, result)
            result.append(root.val)
            self.recurr(root.right, result)
