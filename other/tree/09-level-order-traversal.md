## Links
[Leetcode](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

## Expected Output
See description

## Approach
1. Use Queue to record nodes at each level

**Approach**
```
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList();
        if( root == null ) {
            return res;
        }

        Queue<TreeNode>  q = new LinkedList();

        int size = 0;

        q.offer(root);

        while( !q.isEmpty() ) {
            List<Integer> nodes = new ArrayList();
            size = q.size();

            for(int i = 0; i < size; i++) {
                root = q.poll();

                if( root.left != null ) {
                    q.offer(root.left);
                }

                if( root.right != null ) {
                    q.offer(root.right);
                }

                nodes.add(root.val);
            }
            res.add(nodes);
        }

        return res;
    }
}
```