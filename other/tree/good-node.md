## Links
[Leetcode](https://leetcode.com/problems/count-good-nodes-in-binary-tree)

## Expected Output
No of good nodes in the BTree

### Brute Force
**Approach**:


**code**:
```
class Solution:
    def helper(self, root: TreeNode, maxval: int) -> int:
        if not root:
            return 0
        
        goodNode = 0

        if maxval <= root.val:
            goodNode = 1

        maxval = max(maxval, root.val)

        return goodNode + self.helper(root.left, maxval) + self.helper(root.right, maxval)

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -(10**4 + 1))
```