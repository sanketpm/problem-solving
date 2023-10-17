## Links
[GFG](https://practice.geeksforgeeks.org/problems/odd-even-level-difference/1)

## Expected Output
Output = Sum of Nodes at Odd Level - Sum of Node at even level

## Approach
1. Modified level order traversal

**Approach**
```
class Solution
{
	int getLevelDiff(Node root)
	{
	    int even = 0;
	    int odd = 0;
	    
	    int size = 0;
	    int level = 1;
	    
	    Queue<Node> stk = new LinkedList<>();
	    stk.offer(root);
	    
	    while( !stk.isEmpty() ) {
	        size = stk.size();
	        
	        for(int i = 0; i < size; i++) {
	            root = stk.poll();
	            
	            if(root.left != null) {
	                stk.offer(root.left);
	            }
	            
	            if(root.right != null) {
	                stk.offer(root.right);
	            }
	            
	            if( level % 2 == 0 ) {
	                even += root.data;
	            } else {
	                odd += root.data;
	            }
	        }
	        ++level;
	    }
	    
	    return odd - even;
	}
}
```