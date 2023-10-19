## Links
[Leetcode](https://leetcode.com/problems/diameter-of-binary-tree/description/)

## Expected Output
Diameter of a Binary Tree

## Approach
- Modified Height of a Binary Tree
- Use a variable to store `Max ( L + R )` (this is the diameter)

**Approach**
```
class Solution {

    private int getDiameter(TreeNode root, int[] diameter) {
        if( root == null ) {
            return 0;
        }

        int L = getDiameter(root.left, diameter);
        int R = getDiameter(root.right, diameter);

        if( diameter[0] < L + R){
            diameter[0] = L + R;
        }

        return 1 + Math.max(L, R);
    }

    public int diameterOfBinaryTree(TreeNode root) {
        int[] diameter = new int[1];
        diameter[0] = 0;

        getDiameter(root, diameter);

        return diameter[0];
    }

```

## Python

```
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0  

        def dfs(node):
            nonlocal dia
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            dia = max(dia, left + right)

            return 1 + max(left, right)

        dfs(root)

        return dia
```