## Links
[Leetcode](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

## Expected Output
See the description example

## Approach
1. Convert each node into a 2D graph(Maths), x: Vertical Position, y: Horizontal Position
2. TreeMap: stores `x` values
3. TreeMap: store `y` values
4. PriorityQueue: stores `node` values
`[x: [y: [v1, v2, ...]]]`

**Approach**
```
class Solution {

    class Tuple {
        TreeNode node;
        int x;
        int y;

        Tuple(TreeNode node, int x, int y) {
            this.node = node;
            this.x = x;
            this.y = y;
        }
    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map = new TreeMap<>();
        Queue<Tuple> q = new LinkedList<>();

        q.offer(new Tuple(root, 0, 0));

        while( !q.isEmpty() ) {
            Tuple tuple = q.poll();

            TreeNode curr = tuple.node;
            int x = tuple.x;
            int y = tuple.y;

            map.putIfAbsent(x, new TreeMap<>());
            map.get(x).putIfAbsent(y, new PriorityQueue<>());

            map.get(x).get(y).offer( curr.val);

            if(curr.left != null) {
                q.offer( new Tuple(curr.left, x - 1, y + 1));
            }

            if( curr.right != null ) {
                q.offer( new Tuple(curr.right, x + 1, y + 1));
            }
        }

        List<List<Integer>> res = new ArrayList<>();

        for(TreeMap<Integer, PriorityQueue<Integer>> subTreeMap: map.values() ) {
            res.add( new ArrayList<>() );

            for(PriorityQueue<Integer> pqNodes: subTreeMap.values() ) {
                while( !pqNodes.isEmpty() ) {
                    res.get( res.size() - 1 ).add( pqNodes.poll() );
                }
            }
        }

        return res;
    }
}
```