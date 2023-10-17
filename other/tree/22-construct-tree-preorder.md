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