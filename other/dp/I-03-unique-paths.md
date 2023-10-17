## Links
[Leetcode](https://leetcode.com/problems/unique-paths/)

## Expected Output
No of unique paths to reach `finish`

e.g.:
**Input:**
m = 2, n = 3

**Output:**
3

## Recursive Approach
```
class Solution:
    def pathsToFinish(self, i, j, m, n) -> int:
        if i >= m or j >= n:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1
        
        return self.pathsToFinish(i + 1, j, m , n) + self.pathsToFinish(i, j + 1, m , n)  
        
    def uniquePaths(self, m: int, n: int) -> int:
        return self.pathsToFinish(0, 0, m, n);
        
```

## Memoization - Top Down
```
class Solution:
    def pathsToFinish(self, i, j, m, n, dp) -> int:
        if i >= m or j >= n:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1
        
        if dp[i][j] != -1:
            res = dp[i][j]
            return res
        
        dp[i][j] = self.pathsToFinish(i + 1, j, m , n, dp) + self.pathsToFinish(i, j + 1, m , n, dp)  
        res = dp[i][j]
        return res
        
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [-1]*n for i in range(m)]
        return self.pathsToFinish(0, 0, m, n, dp);
        
```

## Tabulation - Bottom Up
```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0] * n for _ in range(m) ]

        for i in range(n):
            dp[0][i] = 1

        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        res = dp[m - 1][n - 1]
        return res
```

There is only 1 way to reach all cells [0][n] & [m][0] hence mark them as 1,
utilizing them the cells on next level below can reuse the above to reach the result.