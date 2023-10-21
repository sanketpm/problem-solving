## Links
[Leetcode](https://leetcode.com/problems/same-tree/description/)

## Expected Output

## Approach
1. If pNode & qNode both are null => return true;
2. If pNode & qNode both are not null:
   1. Check if they're of same value
   2. recur(pNode-LST, qNode-LST ) && recur(pNode-RST, qNode-RST)
3. Default return false

**Approach**
```
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if( p == null && q == null ) {
            return true;
        }

        if( p!= null && q != null ) {
            return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }

        return false;
    }
}
```

### Python

**Time Complexity:** 
    - `O(min(N, M))`, Where N and M are the sizes of the trees
**Auxiliary Space:** 
    - `O(log min(N, M))`, due to auxiliary stack space used by recursion calls

**Approach**
```
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```