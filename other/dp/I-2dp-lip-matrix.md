## links
[leetcode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## Expected Output

**Dry run:**
```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9]
```

## Recursive Approach

```
class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        vis = set()

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r == m or c == n:
                return 0
            
            if (r, c) in vis:
                return 0
            
            if mat[r][c] <= prev:
                return 0 
            
            vis.add((r, c))
            max_path = 1 + max(
                dfs(r + 1, c, mat[r][c]),
                dfs(r - 1, c, mat[r][c]),
                dfs(r, c + 1, mat[r][c]),
                dfs(r, c - 1, mat[r][c])
            )
            vis.remove((r, c))
            return max_path
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, -1))
        
        return res
```

## Memoization - Top_Down

```
class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        vis = set()
        dp = {}

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r == m or c == n:
                return 0
            
            if (r, c) in vis:
                return 0
            
            if mat[r][c] <= prev:
                return 0 
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            vis.add((r, c))
            max_path = 1 + max(
                dfs(r + 1, c, mat[r][c]),
                dfs(r - 1, c, mat[r][c]),
                dfs(r, c + 1, mat[r][c]),
                dfs(r, c - 1, mat[r][c])
            )
            vis.remove((r, c))
            dp[(r, c)] = max_path
            return max_path
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, -1))
        
        return res
```

## Tabulation - Bottom up

```

```