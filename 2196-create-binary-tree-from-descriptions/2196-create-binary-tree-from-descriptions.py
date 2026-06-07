# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        treemap = {}
        root = {}

        for p, c, lft in descriptions:

            if p not in treemap:
                treemap[p] = TreeNode(p)

            if c not in treemap:
                treemap[c] = TreeNode(c)

            if lft == 1:
                treemap[p].left = treemap[c]
            else:
                treemap[p].right = treemap[c]

            if root.get(p,0) != -1:
                root[p] = 1  

            root[c] = -1

        root_val = 0

        for n,s in root.items():
            if s == 1:
                root_val = n
                break
        return treemap[root_val]            



