## Links
[Leetcode](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)
[GFG](https://practice.geeksforgeeks.org/problems/maximum-sum-leaf-to-root-path/1?)

## Expected Output

### Brute Force
**Approach**:


**code**:
```
class Solution {

    private int sumNumbers(TreeNode root, int sum) {
        if( root == null ) {
            return 0;
        }

        sum = sum * 10 + root.val;

        if( root.left == null && root.right == null ) {
            return sum;
        }

        int left = sumNumbers(root.left, sum);
        int right = sumNumbers(root.right, sum);

        return left + right;
    }
    public int sumNumbers(TreeNode root) {
        if( root == null ) {
            return 0;
        }

        return sumNumbers(root, 0);
    }
}
```

## Python 

**code**:
```
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(cur, sum):
            if not cur:
                return 0
            
            sum = sum * 10 + cur.val

            if not cur.left and not cur.right:
                return sum
            
            left = dfs(cur.left, sum)
            right = dfs(cur.right, sum)

            return left + right
            
        return dfs(root, 0)
```