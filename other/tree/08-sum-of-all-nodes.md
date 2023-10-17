## Links
[GFG](https://practice.geeksforgeeks.org/problems/sum-of-binary-tree/1)

## Expected Output
Sum of all nodes

## Approach
1. CurrVal + recur(root.left) + recur(root.right)

**Approach**
```
class BinaryTree
{
    static int sumBT(Node root){
        if( root == null ) {
            return 0;
        }
        
        return root.data + sumBT(root.left) + sumBT(root.right);
    }
}
```