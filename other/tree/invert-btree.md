## Links
[Leetcode](https://leetcode.com/problems/invert-binary-tree)

## Expected Output


### Brute Force
Return the inverted BTree

**code**:
```
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left, right = root.left, root.right

        root.left = right
        root.right = left 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

### Optimized
**Approach**


**code**:
```

```