## Links
[Leetcode](https://leetcode.com/problems/find-bottom-left-tree-value/description/)

## Expected Output

### Approach
- Modified Level Order Traversal(BFS)
- At each level record the last accessed node

**Time Complexity:** 
    - `O(N)`, each node is accessed once
**Auxiliary Space:** 
    - `O(level_with_max_no_of_nodes)` 

**code**:
```
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()

        q.append(root)

        res = None

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                res = node.val

                if node.right:
                    q.append(node.right) 
                
                if node.left:
                    q.append(node.left) 

        return res
```