"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone(self, node, visited):
        if node in visited:
            return visited[node]
        clone_node = Node(node.val)
        visited[node] = clone_node # build connect between node and clone_node
        for nei in node.neighbors:
            clone_node.neighbors.append(self.clone(nei, visited))
        return clone_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        return self.clone(node, visited)