## Links
[Leetcode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)

## Expected Output

### Approach
Balanced Tree:
    | ht-lst - ht-rst | <= 1

**code**:
```
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def helper(l, r):
            if l > r:
                return None
            
            m = (l + r) // 2

            root = TreeNode(nums[m])

            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)

            return root
        
        return helper(0, n - 1)
```