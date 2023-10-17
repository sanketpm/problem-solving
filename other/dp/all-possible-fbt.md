## links
[leetcode](https://leetcode.com/problems/all-possible-full-binary-trees)

Tags: [Google]

## Expected Output
Full Binary Tree 
- A Binary Tree in which every node has either `No child` or `Two Child` nodes

## Recursive Approach

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def backtrack(n):
            if n == 0:
                return []
            
            if n == 1:
                return [TreeNode(0)]
            
            if n in dp:
                return dp[n]
            
            res = []

            for l in range(n):
                r = (n - 1) - l

                leftTrees = backtrack(l)
                rightTrees = backtrack(r)

                for tL in leftTrees:
                    for tR in rightTrees:
                        res.append(TreeNode(0, tL, tR))
                
            return res
        
        return backtrack(n)
```

## Memoization - Top_Down

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}

        def backtrack(n):
            if n == 0:
                return []
            
            if n == 1:
                return [TreeNode(0)]
            
            if n in dp:
                return dp[n]
            
            res = []

            for l in range(n):
                r = (n - 1) - l

                leftTrees = backtrack(l)
                rightTrees = backtrack(r)

                for tL in leftTrees:
                    for tR in rightTrees:
                        res.append(TreeNode(0, tL, tR))
                
            dp[n] = res

            return dp[n]
        
        return backtrack(n)
```

## Tabulation - Bottom up

```

```