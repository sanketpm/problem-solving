## Links
[Leetcode](https://leetcode.com/problems/symmetric-tree/description/)

## Expected Output
See description

## Approach
- Modified `Are Two Tree Identical`

**Approach**
```
class Solution {

    private boolean isSymmetric(TreeNode p, TreeNode q) {
        if( p == null && q == null ) {
            return true;
        }

        if( p != null && q != null ) {
            return p.val == q.val && isSymmetric(p.left, q.right) && isSymmetric(p.right, q.left);
        }

        return false;
    }
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root.left, root.right);
    }
}
```