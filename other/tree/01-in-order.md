## Links
[Leetcode](https://leetcode.com/problems/binary-tree-inorder-traversal)

## Expected Output
List containing the node values in InOrder's order
### Approach

**code**:
```
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = collections.deque()

        res = []

        while True:
            while root:
                stk.append(root)
                root = root.left
            
            if not stk:
                return res

            root = stk.pop()
            res.append(root.val)
            root = root.right
        
        return res
```