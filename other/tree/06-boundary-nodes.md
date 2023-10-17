## Links
[GFG](https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1)

## Expected Output
All boundary nodes

## Approach
1. Print Left Boundary nodes
2. Print Leaf nodes
3. Print Right boundary nodes

```
class Solution
{
    boolean isLeaf(Node root) {
        return (root.left == null) && (root.right == null);
    }
    
    void leftboundary(Node curr, ArrayList<Integer> res) {
        while( curr != null ) {
            if( !isLeaf(curr) ) {
                res.add(curr.data);
            }

            if(curr.left != null) {
                curr = curr.left;
            } else {
                curr = curr.right;
            }
        }
    }
    
    void leaves(Node node, ArrayList<Integer> res) {
        if( node == null ) {
            return;
        }
        
        if( isLeaf(node) ) {
            res.add(node.data);
        }
        
        leaves(node.left, res);
        leaves(node.right, res);
    }
    
    void rightboundary(Node curr, ArrayList<Integer> res) {
        ArrayList<Integer> temp = new ArrayList<>();

        while( curr != null ) {
            if( !isLeaf(curr) ) {
                temp.add(curr.data);
            }
            
            if(curr.right != null) {
                curr = curr.right;
            } else {
                curr = curr.left;
            }
        }
        
        Collections.reverse(temp);
        res.addAll(temp);
    }
    
	ArrayList <Integer> boundary(Node node)	{

	    if( node == null ) {
	        return null;
	    }

	    if( isLeaf(node) ) {
	        return new ArrayList<>(Arrays.asList(node.data));
	    }
	    

	    ArrayList<Integer> res = new ArrayList<>();
	    res.add(node.data);
	    
	    
	    leftboundary(node.left, res);
	    leaves(node, res);
	    rightboundary(node.right, res);
	    
	    return res;
	}
}
```