## Links
[Leetcode](https://leetcode.com/problems/maximum-width-of-binary-tree/description/)

## Expected Output
See description

## Approach


**Approach**
```
class Solution {

    class Tuple {
        TreeNode node;
        int pos;
        int level;

        Tuple(TreeNode node, int pos, int level) {
            this.node = node;
            this.pos = pos;
            this.level = level;
        }
    }

    public int widthOfBinaryTree(TreeNode root) {
        if( root == null ) {
            return 0;
        }
        
        Queue<Tuple> q = new LinkedList<>();
        
        int res = 0;
        int level = -1;
        int firstPosition = 0;
        int width  = 0;

        q.offer(new Tuple(root, 1, 0));

        while( !q.isEmpty() ) {
            Tuple tuple = q.poll();
            TreeNode node = tuple.node;
            

            if( level < tuple.level ) {
                level = tuple.level;
                firstPosition = tuple.pos; 
            }

            width = tuple.pos - firstPosition + 1;

            res = Math.max(res, width);

            if( tuple.node.left != null ) {
                q.offer(new Tuple(tuple.node.left, tuple.pos * 2, tuple.level + 1));
            }

            if( tuple.node.right != null ) {
                q.offer(new Tuple(tuple.node.right, tuple.pos * 2 + 1, tuple.level + 1));
            }
        }

        return res;
    }
}
```