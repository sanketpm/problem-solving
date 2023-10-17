## links
[leetcode](https://leetcode.com/problems/minimum-path-sum/description/)

## Expected Output


## Recursive Approach

```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if i == m or j == n:
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            right = grid[i][j] + dfs(i + 1, j)
            down = grid[i][j] + dfs(i, j + 1)

            res = min(right, down)

            return res

        return dfs(0, 0)
```

## Memoization - Top_Down

```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = {}
        
        def dfs(i, j):
            if i == m or j == n:
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            right = grid[i][j] + dfs(i + 1, j)
            down = grid[i][j] + dfs(i, j + 1)

            dp[(i, j)] = min(right, down)

            return dp[(i, j)]

        return dfs(0, 0)
```

## Tabulation - Bottom up

```

```