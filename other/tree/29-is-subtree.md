## Links
[Leetcode](https://leetcode.com/problems/subtree-of-another-tree/)

## Expected Output

### Approach
**Approach**:
1. Find the matching node_val in main-tree & sub-tree & call & recursively check if they're identical

**code**:
```
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stk = collections.deque()

        while True:
            while root:
                stk.append(root)
                root = root.left
            
            if not stk:
                break
            
            root = stk.pop()

            if root.val == subRoot.val and self.isSameTree(root, subRoot):
                return True

            root = root.right

        return False 
```