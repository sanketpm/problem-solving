## Links
[Leetcode](https://leetcode.com/problems/merge-two-binary-trees)

## Expected Output

### Approach

**code**:
```
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        t1.val += t2.val
        
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1
```