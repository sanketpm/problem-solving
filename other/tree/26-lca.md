## Links
[Leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

## Expected Output
See description

## Approach
1. At every node we check if it's LST has encountered a matching value & right subtree has encountered a matching value. We do this at each node
2. If LST-has-value = true && RST-has-value => record the current node

### Brute Force

### Optimized

**Approach**
```
class Solution {

    private TreeNode lca;
    
    Solution() {
        this.lca = null;
    }

    private boolean lca(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) {
            return false;
        }

        int left = lca(root.left, p, q) ? 1 : 0;
        int right = lca(root.right, p, q) ? 1 : 0;
        int mid = ( root == p || root == q ) ? 1 : 0;

        if( left + right + mid >= 2 ) {
            this.lca = root;
        }

        return left + right + mid > 0;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        lca(root, p, q);

        return this.lca;
    }
}
```

## Python

```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            nonlocal res
            if not node:
                return False
            
            m = 1 if node in [p, q] else 0 
            l = 1 if dfs(node.left) else 0 
            r = 1 if dfs(node.right) else 0 

            if l + m + r == 2:
                res = node
            
            return l + m + r > 0
        
        dfs(root)

        return res
```