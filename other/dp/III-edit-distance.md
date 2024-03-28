## links
[leetcode](https://leetcode.com/problems/minimum-path-sum/description/)

## Expected Output
- Minimum Operations to convert `word1` t `word2`
- Operations allowed:
    1. Insert
    2. Delete
    3. Replace


> This problem is an extension of Longest Common Subsequence

## Recursive Approach

```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m == 0 and n == 0:
            return 0
        
        if m == 0 or n == 0:
            return max(m, n)
        
        def dfs(i, j):
            if i == m and j == n:
                return 0
            
            if i == m or j == n:
                return max(m - i, n - j)
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(
                    dfs(i, j + 1),
                    dfs(i + 1, j),
                    dfs(i + 1, j + 1)
                )
        
        return dfs(0, 0)
```

## Memoization - Top_Down

```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m == 0 and n == 0:
            return 0
        
        if m == 0 or n == 0:
            return max(m, n)

        dp = {}
        
        def dfs(i, j):
            if i == m and j == n:
                return 0
            
            if i == m or j == n:
                return max(m - i, n - j)
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(
                    dfs(i, j + 1),
                    dfs(i + 1, j),
                    dfs(i + 1, j + 1)
                )
            
            return dp[(i, j)]
            
        return dfs(0, 0)
```

## Tabulation - Bottom up

```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [ [float('inf')] * (n + 1) for _ in range(m + 1) ]

        for i in range(n + 1):
            dp[m][i] = n - i

        for i in range(m + 1):
            dp[i][n] = m - i

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min( 
                        dp[i][j + 1], 
                        dp[i + 1][j], 
                        dp[i + 1][j + 1]
                    )
        return dp[0][0]
```