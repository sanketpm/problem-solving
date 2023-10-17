
## Links
[Leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

## Expected Output


### Approach
- Utilize the BST property.
- The node where p & q both lie on either side it the LCA.
- At every non LCA node, both p & q lie either of on left-side or on right-side 

**code**:
```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        
        return None
                
```