from collections import defaultdict
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
  
        root = 1

        def create_node(val,parent):
            node = {'val':val, 'children': []}
            for neighbor in adj[val]:
                if neighbor != parent:
                    node['children'].append(create_node(neighbor, val))
            return node    

        tree = create_node(root, None) 


        def maxdepth(tree):
            if not tree:
                return 0

            if not tree["children"]:
                return 0

            maxdepthval = max(maxdepth(child) for child in tree['children'])  
            return maxdepthval+1

        maxdepth = maxdepth(tree)

        return (2 ** (maxdepth - 1)) % (10**9 + 7)
        

