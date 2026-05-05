# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        else:
            dict1 = {}
            stack = [root]
            while stack:
                current = stack.pop()
                if current.val in dict1:
                    dict1[current.val] = dict1.get(current.val,0)+1
                else:
                    dict1[current.val ] = 1          
                if current.left:
                    stack.append(current.left)
                if current.right:        
                    stack.append(current.right)
            
            mode = 0
            lst = []
            for key, value in dict1.items():
                if  value > mode:
                    mode = value

            return [k for k,v in dict1.items() if v == mode]        
