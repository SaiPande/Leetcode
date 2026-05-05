# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lsttree1 = []
        lsttree2 = []

        lsttree1 = self.preordertree(p, [])
        lsttree2 = self.preordertree(q, [])

        return lsttree1 == lsttree2
            
    def preordertree(self, t: Optional[TreeNode], lsttree: list) -> list:
        node = t
        if node:
            lsttree.append(t.val)
            self.preordertree(t.left, lsttree)
            self.preordertree(t.right, lsttree)
        else: 
            lsttree.append(None)

        return lsttree    
            