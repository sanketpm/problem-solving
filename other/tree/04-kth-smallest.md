## Links
[Leetcode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

## Expected Output
Kth smallest element

## Approach
- Modified Iterative InOrder Traversal

**Approach**
```
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        LinkedList<TreeNode> stk = new LinkedList<>();

        while( true ) {
            while(root != null) {
                stk.push(root);
                root = root.left;
            }

            if( stk.isEmpty() ) {
                return -1;
            }

            root = stk.pop();
            k = k - 1;
            if( k == 0 ) {
                return root.val;
            }

            root = root.right;
        }
    }
}
```

### Python
- modified iterative inorder traversal.

**code**
```
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = collections.deque()

        while True:
            while root:
                stk.append(root)
                root = root.left
            
            root = stk.pop()
            k = k - 1

            if k == 0:
                return root.val
            
            root = root.right

        return -1
```