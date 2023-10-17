## Links
[GFG](https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1)

## Expected Output

## Brute Force Approach

## Optimized Approach

**Brute force**
```

```

**Optimized Approach**
```
class GfG
{
    private Node sort(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node temp = dummy;
        
        while(l1 != null && l2 != null) {
            if(l1.data < l2.data) {
                temp.bottom = l1;
                l1 = l1.bottom;
            } else {
                temp.bottom = l2;
                l2 = l2.bottom;
            }
            temp = temp.bottom;
        }
        if(l1 == null) {
            temp.bottom = l2;
        } else {
            temp.bottom = l1;
        }
        return dummy.bottom;
    }
    Node flatten(Node root) {
        if(root == null || root.next == null) {
            return root;
        }
        
        Node right = flatten(root.next);
        
        Node res = sort(root, right);
        
        return res;
    }
}
```