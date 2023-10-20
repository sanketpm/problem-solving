## Links
[Leetcode](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/submissions/958506110/)

## Expected Output

## Approach


**Approach**
```
class Solution {
    class Index {
        int val = 0;

        Index(int val) {
            this.val = val;
        }
    }

    private TreeNode bstFromPreorder(int[] preorder, Index index, int bound, int length) {
        if(index.val == length || preorder[index.val] > bound ) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[index.val]);
        index.val += 1;

        root.left = bstFromPreorder(preorder, index, root.val, length);
        root.right = bstFromPreorder(preorder, index, bound, length);

        return root;
    }

    public TreeNode bstFromPreorder(int[] preorder) {
        Index i = new Index(0);

        return bstFromPreorder(preorder, i, Integer.MAX_VALUE, preorder.length);
    }
}
```

## Python

```
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> Optional[TreeNode]:
        n = len(pre)
        i = 0

        def dfs(ub):
            nonlocal i
            if i == n or pre[i] > ub:
                return None

            root = TreeNode(pre[i])
            i += 1

            root.left = dfs(root.val)
            root.right = dfs(ub)

            return root
        
        return dfs(float('inf'))
```