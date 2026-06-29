# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        current = root
        
        optlist = []
        level = 0
        maxval = 0

        self.levelorderrec(root, 0, optlist)

        return max(range(len(optlist)), key=lambda i: sum(optlist[i])) + 1

    def levelorderrec(self, root: Optional[TreeNode], level: int, optlist: List[List[int]]):
        if not root:
            return

        if len(optlist)<= level:
            optlist.append([])

        optlist[level].append(root.val)
       
        self.levelorderrec(root.left, level+1, optlist)
        self.levelorderrec(root.right, level+1, optlist)