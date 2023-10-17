## Links
[Leetcode](https://leetcode.com/problems/validate-binary-search-tree)

## Expected Output

### Brute Force
**Approach**:


**code**:
```
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min, max):
            if not root:
                return True
            
            if not (root.val > min and root.val < max):
                return False
            
            return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)
        
        return dfs(root, float('-inf'), float('inf'))
        
```