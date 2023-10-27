## Links
[Leetcode](https://leetcode.com/problems/path-sum/description/)

## Expected Output

### Approach
- Modified DFSw

**Time Complexity:** 
    - `O(N)`, DFS
**Auxiliary Space:** 
    - `O(N)`, case: `skewed-tree`

**code**:
```
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val 

        if not root.left and not root.right:
            return targetSum == 0

        L = self.hasPathSum(root.left, targetSum)
        R = self.hasPathSum(root.right, targetSum)

        return L or R
```