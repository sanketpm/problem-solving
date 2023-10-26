## Links
[Leetcode](https://leetcode.com/problems/trim-a-binary-search-tree/description/)

## Expected Output

### Approach
**Time Complexity:** 
    - `O(N)`, DFS
**Auxiliary Space:** 
    - `O(N)`, case: left or right-skewed tree with `low = root.val` and `high = val_right_or_left_most_node`, whole tree will exist in recursive stack

**code**:
```
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
```

### Optimized
**Approach**

**Time Complexity:** 
    - `O(N)`, Where N is ..
**Auxiliary Space:** 
    - `O(N)`, due to ...

**code**:
```

```