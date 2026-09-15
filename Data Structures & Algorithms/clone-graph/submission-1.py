"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        visited = {}
        
        def rec(n):
            if n in visited:
                return visited[n]
            
            newN = Node(n.val)
            visited[n] = newN
            for node in n.neighbors:
                newN.neighbors.append(rec(node))
            return newN
        
        return rec(node)