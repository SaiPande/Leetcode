# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        sm = 0
        stack = []
        stack.append([root, False])
        subtree_data = {}
        output = 0

        count = 0
        
        while stack:
            current, visited = stack.pop()
            if not current:
                continue

            if visited:
                left_sum, left_count = subtree_data.get(current.left, [0, 0])
                right_sum, right_count = subtree_data.get(current.right, [0, 0])    

                total_sum = current.val + left_sum + right_sum
                total_count = 1+ left_count + right_count

                subtree_data[current] = [total_sum, total_count]

                if total_sum // total_count == current.val:
                    output += 1
            else:
                stack.append([current, True])
                stack.append([current.right, False])
                stack.append([current.left, False])
                
        return output  