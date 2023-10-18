## Links
[Leetcode](https://leetcode.com/problems/binary-tree-right-side-view/description/)
[GFG](https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1)

## Expected Output
All nodes when viewed from right side

## Approach - Level Order Traversal
1. Level Order Traversal
2. Keep updating the `node` value for each iteration of the level-queue, last value in `node` store in result

```
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new LinkedList<>();

        if(root == null) {
            return res;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while(!q.isEmpty()) {
            int node = -101;
            int size = q.size();

            for(int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                node = curr.val;

                if(curr.left != null) {
                    q.offer(curr.left);
                }

                if(curr.right != null) {
                    q.offer(curr.right);
                }
            }

            res.add(node);
        }

        return res; 
    }
}
```

## Appraoch
1. Have a `levelIndicatror` (global)
2. Have a `currLevel`
3. Record the node IFF: `levelIndicator < currLevel` & update levelIndictor to currLevel
4. Recur(left) then Recur(right), vice versa for Right View

**Approach**
```
// https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1
class Solution{
    int levelIndicator = -1;
    
    void rightView(Node root, int currLevel, ArrayList<Integer> res) {
        if(root == null) {
            return;
        }
        
        if(levelIndicator < currLevel) {
            res.add(root.data);
            levelIndicator = currLevel;
        }
        
        rightView(root.right, currLevel + 1, res);
        rightView(root.left, currLevel + 1, res);
    }
    
    ArrayList<Integer> rightView(Node node) {
        ArrayList<Integer> res = new ArrayList<>();
        
        if(node == null) {
            return res;
        }
        
        rightView(node, 0, res);
        
        return res;
    }
}
```

## Python
**Iterative:**

```
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        que = collections.deque()
        que.append(root)

        while que:
            size = len(que)

            for i in range(size):
                node = que.popleft()

                if i == 0:
                    res.append(node.val)

                if node.right:
                    que.append(node.right)

                if node.left:
                    que.append(node.left)
        
        return res
```