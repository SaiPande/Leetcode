# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        else:
            stack = [(root,str(root.val))]
            finallist = []
           
            while stack:
                current,pathstring = stack.pop()
                if current.right:
                    stack.append((current.right, pathstring+"->"+str(current.right.val)))
                    #pathstring = pathstring+"->"
                if current.left:
                    stack.append((current.left, pathstring+"->"+str(current.left.val)))
                if not current.left and not current.right:
                    finallist.append(pathstring)    
        return finallist
