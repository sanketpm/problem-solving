## links
[leetcode](https://leetcode.com/problems/unique-paths-ii/description/)

## Expected Output


## Recursive Approach

```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        def dfs(i, j):
            if i == m or j == n or obstacleGrid[i][j] == 1:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            right = dfs(i + 1, j)
            down = dfs(i, j + 1)

            return right + down

        return dfs(0, 0)
```

## Memoization - Top_Down

```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = {}
        
        def dfs(i, j):
            if i == m or j == n or obstacleGrid[i][j] == 1:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            right = dfs(i + 1, j)
            down = dfs(i, j + 1)

            dp[(i, j)] = right + down

            return dp[(i, j)]

        return dfs(0, 0)
```

## Tabulation - Bottom up

```

```