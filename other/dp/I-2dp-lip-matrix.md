## links
[leetcode]()

## Expected Output


## Recursive Approach

```
class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        def dfs(r, c, prev):
            if ( r < 0 or c < 0 or
                r == m or c == n or
                mat[r][c] <= prev ):
                return 0
            
            res = 1

            maxPath = max(
                dfs(r + 1, c, mat[r][c]),
                dfs(r - 1, c, mat[r][c]),
                dfs(r, c + 1, mat[r][c]),
                dfs(r, c - 1, mat[r][c]),
            )

            return res + maxPath

        LIP = float('-inf')
        for r in range(m):
            for c in range(n):
                LIP = max(LIP, dfs(r, c, -1) )
        
        return LIP
```

## Memoization - Top_Down

```
class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        dp = {}

        def dfs(r, c, prev):
            if ( r < 0 or c < 0 or
                r == m or c == n or
                mat[r][c] <= prev ):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1

            maxPath = max(
                dfs(r + 1, c, mat[r][c]),
                dfs(r - 1, c, mat[r][c]),
                dfs(r, c + 1, mat[r][c]),
                dfs(r, c - 1, mat[r][c]),
            )

            dp[(r, c)] = res + maxPath

            return dp[(r, c)]

        LIP = float('-inf')
        for r in range(m):
            for c in range(n):
                LIP = max(LIP, dfs(r, c, -1) )
        
        return LIP
```

## Tabulation - Bottom up

```

```