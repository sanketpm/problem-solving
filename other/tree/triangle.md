## Links
[Leetcode](https://leetcode.com/problems/triangle)

## Expected Output

### Brute Force
**Approach**:


**code**:
```
class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        n = len(tri)

        def dfs(lvl, i):
            if lvl == n:
                return 0
            
            left = dfs(lvl + 1, i)
            right = dfs(lvl + 1, i + 1)

            return tri[lvl][i] + min(left, right)
        
        return dfs(0, 0)
```

### Memoized
**Approach**


**code**:
```
class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        n = len(tri)

        dp = {}

        def dfs(lvl, i):
            if lvl == n:
                return 0
            
            if (lvl, i) in dp:
                return dp[(lvl, i)]
            
            left = dfs(lvl + 1, i)
            right = dfs(lvl + 1, i + 1)

            dp[(lvl, i)] = tri[lvl][i] + min(left, right)

            return dp[(lvl, i)]
        
        return dfs(0, 0)
```

**Questions:**
1. Where the sub-problems, show one example to prove this is DP questions?
2. 