## Links
[GFG](https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1)

## Expected Output
All nodes when viewed from Left Side

## Approach - Level Order Traversal
1. Level Order Traversal
2. Keep updating the `node` value for each iteration of the level-queue, last value in `node` store in result

```
class Tree {
    ArrayList<Integer> leftView(Node root) {
        ArrayList<Integer> res = new ArrayList<>();

        if(root == null) {
            return res;
        }

        Queue<Node> q = new LinkedList<>();
        q.offer(root);

        while(!q.isEmpty()) {
            int node = -101;
            int size = q.size();

            for(int i = 0; i < size; i++) {
                Node curr = q.poll();
                node = curr.data;

                if(curr.right != null) {
                    q.offer(curr.right);
                }
                
                if(curr.left != null) {
                    q.offer(curr.left);
                }

            }

            res.add(node);
        }

        return res; 
    }
}
```

## Approach - Space Optimised
1. Have a `levelIndicatror` (global)
2. Have a `currLevel`
3. Record the node IFF: `levelIndicator < currLevel` & update levelIndictor to currLevel
4. Recur(left) then Recur(right), vice versa for Right View

**Approach**
```
class Tree
{
    int levelIndicator = -1;
    
    void leftView(Node root, int currLevel, ArrayList<Integer> res) {
        if(root == null) {
            return;
        }
        
        if( levelIndicator < currLevel) {
            res.add(root.data);
            levelIndicator = currLevel;
        }
        
        leftView(root.left, currLevel+1, res);
        leftView(root.right, currLevel+1, res);
    }
    
    ArrayList<Integer> leftView(Node root) {
      ArrayList<Integer> res = new ArrayList<>();
      
      if( root == null ) {
          return res;
      }
      
      leftView(root, 0, res);
      
      return res;
    }
}
```