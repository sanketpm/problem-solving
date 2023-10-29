**code**
```
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def buildTree(self, inp: list[int]) -> Optional['TreeNode']:
        n = len(inp)
        i = 0

        def dfs(i):
            if i >= n:
                return None
            
            root = TreeNode(inp[i])
            root.left = dfs(2 * i + 1)
            root.right = dfs(2 * i + 2)

            return root
        
        return dfs(0)
```

```
inp = [1, 2, 3, 4, 5, 6, 7]
root = TreeNode().buildTree(inp)
```