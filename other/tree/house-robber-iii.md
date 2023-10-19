## Links
[Leetcode](https://leetcode.com/problems/house-robber-iii/)

## Expected Output

### Approach

**code**:
```
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            withRoot = node.val + left[1] + right[1]
            withoutRoot = max(left) + max(right)

            return [withRoot, withoutRoot]
        
        return max(dfs(root))
```
