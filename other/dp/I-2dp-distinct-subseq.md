## links
[leetcode](https://leetcode.com/problems/distinct-subsequences)

## expected output


## recursive approach

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        def dfs(i, j):
            if j == n:
                return 1

            if i == m:
                return 0

            if s[i] == t[j]:
                take = dfs(i + 1, j + 1) 
                dntTake = dfs(i + 1, j)
                return take + dntTake
            else:
                return dfs(i + 1, j)
            
        return dfs(0, 0)
```

## memoization - top down

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = {}

        def dfs(i, j):
            if i == m and j == n:
                return 1
            
            if j == n:
                return 1
            
            if i == m:
                return 0 
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            pick, dnt_pick = 0, 0
            
            if s[i] == t[j]:
                pick = dfs(i + 1, j + 1)
            
            dnt_pick = dfs(i + 1, j)

            dp[(i, j)] = pick + dnt_pick
            return dp[(i, j)]
            
        return dfs(0, 0)
```

## tabulation - bottom up (1)

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [ [0] * (n + 1) for _ in range(m + 1) ]

        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]
```

## tabulation - bottom up (2)

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [ [0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pick, dnt_pick = 0, 0
                if s[i - 1] == t[j - 1]:
                    pick = dp[i - 1][j - 1]
                dnt_pick = dp[i - 1][j]
                dp[i][j] = pick + dnt_pick
        
        return dp[m][n]
```