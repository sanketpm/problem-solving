## Links
[Leetcode](https://leetcode.com/problems/clone-graph/description/)

## Expected Output
Completely Cloned Graph

## Approach
1. Have a mapping of `given-node` to `clonedNode`
2. Use DFS:
    1. If the node in iteration exist in `oldToMap` if yes: get that clonedNode
    2. If node doesn't exist in `oldToMap` create a new-clonedNode & a mapping for the givenNode => newly clonedNode

```
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        oldToNew = {}

        def dfsClone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            clonedNode = Node(node.val)
            oldToNew[node] = clonedNode

            for nb in node.neighbors:
                clonedNeighbor = dfsClone(nb)
                clonedNode.neighbors.append(clonedNeighbor)
            
            return clonedNode
        
        dfsClone(node)

        return oldToNew[node]
```