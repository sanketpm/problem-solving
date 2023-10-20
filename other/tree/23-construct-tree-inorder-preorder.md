## Links
[Leetcode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

## Expected Output

## Approach


>NOTE: Dry run - have size of Left Subtree & Right subtree be different. 
### Brute Force

### Optimized

**Approach**
```
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

## Python

```
class Solution:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
        if not pre or not ino:
            return None
        
        root = TreeNode(pre[0])

        nLst = ino.index(pre[0])

        root.left = self.buildTree(pre[1 : nLst + 1], ino[:nLst])
        root.right = self.buildTree(pre[(nLst + 1):], ino[(nLst + 1):])

        return root
```