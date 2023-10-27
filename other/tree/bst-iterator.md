## Links
[Leetcode](https://leetcode.com/problems/binary-search-tree-iterator)

## Expected Output

### Approach
- Modified Iterative Inorder Traversal

> note: At any given instance, the treenode pointer will point to the lowest node in BST. Therefore, when next() is executed the ptr moves to the right node & recursively/iteratively moves to the lowest node of that sub-tree

**Time Complexity:** 
- `hasNext()`: `O(1)`
- `next()`: `O(1)`

**Auxiliary Space:** 
- `hasNext()` : `O(h)`
- `next()` : `O(h)`

**code**:
```
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = collections.deque()
        while root:
            self.stk.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stk.pop()
        cur = res.right
        while cur:
            self.stk.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return len(self.stk) > 0
```