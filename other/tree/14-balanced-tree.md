## Links
[Leetcode](https://leetcode.com/problems/balanced-binary-tree)
[GFG](https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1)

## Expected Output
True: If Tree is Balanced Tree\
False: If Tree is unBalanced

## Approach
**Q** When is a Tree balanced?
- `At any given node, difference between height of Left subtree & height of right subtree is <= 1 [0, 1]`.
- Above statement holds true for all nodes in a tree, do the exactly the same at every node as described below:

1. At Each Node
   1. Get Height of Left subtree(LST)
   2. Get Height of Right subtree(RST)
2. Return Statement
   - isCurrentNodeBalanced = `( | ht_lst - ht_rst | <= 1 )` &&
   - isLeftSubtreeBalanced = `isBalanced(root.left)` &&
   - isRightSubtreeBalanced = `isBalanced(root.right)`

> Modified Height of a Binary-Tree with Balance Check on Current Node

**Approach**
```
class Tree
{
    int height(Node root) {
        if( root == null ) {
            return 0;
        }
        
        return 1 + Math.max(height(root.left), height(root.right));
    }
    
    boolean isBalanced(Node root) {
        if(root == null) {
            return true;
        }
        
        int lh = height(root.left);
        int rh = height(root.right);
        
        return Math.abs(lh - rh) <= 1 && isBalanced(root.left) && isBalanced(root.right);
    }
}
```

## Python
```
class Solution:
    def height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lh = self.height(root.left)
        rh = self.height(root.right)

        return abs(lh - rh) in [0, 1] and self.isBalanced(root.left) and self.isBalanced(root.right)
```