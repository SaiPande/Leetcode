# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            outputlist = []
            outputlist = self.postorder(root,outputlist)  
        return outputlist      
        
    def postorder(self, root: Optional[TreeNode], outputlist: List) -> List[int]:    
        if root:
            self.postorder(root.left, outputlist)
            self.postorder(root.right, outputlist)
            outputlist.append(root.val)
        return outputlist    