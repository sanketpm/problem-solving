## Links
[Leetcode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/)

## Expected Output

### Approach
- BFS

**Time Complexity:** 
    - `O(N)`, N = Total number of nodes in Btree
**Auxiliary Space:** 
    - `O(2^k)`, k = Level of Btree  

**code**:
```
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = collections.deque([])
        q.append(root)

        while q:
            size = len(q)

            next = None
            for i in range(size):
                q[i].next = next
                next = q[i]
            
            for i in range(size):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                    
                if node.left:
                    q.append(node.left)
        return root
```