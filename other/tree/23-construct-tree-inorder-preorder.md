## Links
[Leetcode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

## Expected Output

## Approach


>NOTE: Dry run - have size of Left Subtree & Right subtree be different. 
### Brute Force

### Optimized

**Approach**
```
 /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    private TreeNode buildTree(int[] pos, int pStart, int pEnd, 
                                int[] in, int iStart, int iEnd,
                                Map<Integer, Integer> iMap) {
        if( iStart > iEnd || pStart > pEnd ) {
            return null;
        }

        TreeNode root = new TreeNode(pos[pEnd]);
        int iPos = iMap.get(pos[pEnd]);
        int nLst = iPos - iStart;

        root.left = buildTree(pos, pStart , pStart + nLst - 1,
                                in, iStart, iPos - 1, iMap);
        root.right = buildTree(pos, pStart + nLst, pEnd - 1, 
                                in, iPos + 1, iEnd, iMap);


        return root;
    }
    
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        Map<Integer, Integer> iMap = new HashMap<>();
        int n = inorder.length;

        for(int i = 0; i < n; i++) {
            iMap.put(inorder[i], i);
        }

        return buildTree(postorder, 0, n - 1, inorder, 0, n - 1, iMap);
    }
}
```