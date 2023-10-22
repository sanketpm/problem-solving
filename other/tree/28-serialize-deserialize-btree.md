## Links
[Leetcode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)

## Expected Output
Serialize: String representation of Tree
Deserialize: Binary Tree from tree string

![img](../../images/serdeser.jpg)
## Approach
1. Use Level Order Traversal (Serialize & Deserialize)
2. `null` -> `#` in serialization
3. `#` -> `null` in deserialization

**Approach**
```
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if( root == null ) {
            return "";
        }
        Queue<TreeNode> q = new LinkedList<>();
        StringBuilder res = new StringBuilder();
        TreeNode node;

        q.add( root );

        while( !q.isEmpty() ) {
            node = q.poll();

            if( node == null ) {
                res.append("#,");
                continue;
            }

            res.append(node.val+",");

            q.add(node.left);
            q.add(node.right);
        }

        return res.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if( data.equals("") ) {
            return null;
        }

        Queue<TreeNode> q = new LinkedList<>();
        String[] values = data.split(",");

        TreeNode root = new TreeNode(Integer.parseInt(values[0]));
        
        q.add(root);

        for(int i = 1; i < values.length; i++ ) {
            TreeNode parent = q.poll();

            if( !values[i].equals("#")) {
                parent.left = new TreeNode(Integer.parseInt(values[i]));
                q.add(parent.left);
            }

            ++i;
            if( !values[i].equals("#")) {
                parent.right = new TreeNode(Integer.parseInt(values[i]));
                q.add(parent.right);
            }
        }

        return root;
    }
}
```

### Python
1. Use Pre-order traversal to serialize & deserialize Tree

**code**
```
class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if node is None:
                res.append('#')
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        ser = ','.join(res)
        return ser

    def deserialize(self, data):
        nodes = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            if nodes[i] == '#':
                i += 1
                return None

            node = TreeNode(int(nodes[i]))
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
```