## Links
[InterviewBit](https://www.interviewbit.com/problems/path-to-given-node/)

## Expected Output
List of Path (root --> .. --> targetNode)

## Approach
1. Kind of modified Height Balanced true
2. Using || between recurLeft & recurRight


**Approach**
```
public class Solution {
    
    private boolean hasNode(TreeNode root, int node, ArrayList<Integer> res) {
        if( root == null ) {
            return false;
        }
        
        res.add(root.val);
        
        if( root.val == node ) {
            return true;
        }
        
        if( hasNode(root.left, node, res) || hasNode(root.right, node, res) ) {
            return true;
        }
        
        res.remove( res.size() - 1);
        return false;
    }
    
    public ArrayList<Integer> solve(TreeNode A, int B) {
        ArrayList<Integer> res = new ArrayList<>();
        
        hasNode(A, B, res);
        
        return res;
    }
}
```

**NOTE**
1. Short Circuit Evaluation
**_code1_**
```
boolean condition1 = false;

if( condition1 && condition2 ) {
    //
}
```
Q1. Will condition2 be executed?\
A. NO

**_code2_**
```
boolean condition1 = true;

if( condition1 || condition2 ) {
    //
}
```
Q2. Will condition2 be executed?\
A. NO