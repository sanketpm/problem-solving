## Links
[GFG](https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1)

## Expected Output
List of all nodes when viewed from top

## Approach
- Modified Vertical Order Traversal

**Approach**
```
class Solution
{
    static class Tuple {
        Node node;
        int x;
        
        Tuple(Node node, int x) {
            this.node = node;
            this.x = x;
        }
    }
    static ArrayList<Integer> topView(Node root) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        Queue<Tuple> q = new LinkedList<>();
        
        q.offer(new Tuple(root, 0));
        
        while( !q.isEmpty() ) {
            Tuple tuple = q.poll();
            Node curr = tuple.node;
            int x = tuple.x;
            
            map.putIfAbsent(x, curr.data);
            
            if( curr.left != null ) {
                q.offer( new Tuple( curr.left, x - 1));
            }
            
            if( curr.right != null ) {
                q.offer( new Tuple(curr.right, x + 1));
            }
        }
        
        ArrayList<Integer> res = new ArrayList<>();
        
        for(Integer nodeVal: map.values() ) {
            res.add(nodeVal);
        }
        
        return res;
    }
}
```