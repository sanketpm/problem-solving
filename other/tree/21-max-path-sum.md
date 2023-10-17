## Links
[Leetcode](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

## Expected Output
See description 

## Approach
1. Bottom up approach
2. Modified ht of a binary tree
3. At any node we calculate the sum of (currnode.val + LST_Val + RST_val) & store it in a global max
4. We return to parent node currnode.val + max(LST, RST)

>LST: Left subtree, RST: Right subtree

**Approach**

**Solution1:**
```
class Solution:
    def maxpathsum(self, root: Optional[TreeNode], res: List[int]) -> int:
        if not root:
            return 0
        
        l = self.maxpathsum(root.left, res) 
        r = self.maxpathsum(root.right, res)
        
        curr = root.val + l + r

        res[0] = max(res[0], root.val, curr, root.val + l, root.val + r)

        return max(root.val, root.val + l, root.val + r)  

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-float('inf')] 

        self.maxpathsum(root, res)

        return res[0]
```

**solution2**:
```
class Solution {
    private int max = Integer.MIN_VALUE;

    private int maxpathsum(TreeNode root) {
        if( root == null ) {
            return 0;
        }

        int leftsum = maxpathsum(root.left);
        int rightsum = maxpathsum(root.right);

        leftsum = Math.max(leftsum, 0);
        rightsum = Math.max(rightsum, 0);

        int currsum = leftsum + rightsum + root.val;

        if( max < currsum ) {
            max = currsum;
        }

        return root.val + Math.max(leftsum, rightsum);
    }
    public int maxPathSum(TreeNode root) {
        if(root == null) {
            return 0;
        }

        maxpathsum(root);

        return max;
    }
}
```

**Questions**
Why did you assign 0 when leftsum/rightsum were < 0? Line 24, 25.
- If the value of leftsum/rightsum < 0, it's better to reset it to ZERO, Why?
1. assume root = +'ve value, in that case, we should not reduce it's value by adding with a -'ve number
2. assume rrot = -'ve value, in that case, we should not increase the -'ve value by adding with some other -'ve value
3. Best case: If you encounter -'ve number : reset it to ZERO

Try the below cases & the logic for reseting leftMax/rightMax to Zero will become apparant.

**Edge Cases**
1. [1, -1, -2]
2. [-100, -1, -50]
3. [1, 2, 4]
4. [5, 1, 2]
