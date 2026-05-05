"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        else:
            outputlist = []
            self.preorderrec(root, outputlist) 
            return outputlist  
                  

    def preorderrec(self, root:'Node', outputlist: List) -> None:
        if not root:
            return

        else:
            outputlist.append(root.val)
                
            for i in root.children:
                self.preorderrec(i, outputlist) 
                

