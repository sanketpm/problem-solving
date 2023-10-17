## links
[leetcode](https://leetcode.com/problems/paint-house/)

## Expected Output
Minimum cost to paint all the houses

Constraints:
2 Adjacent houses cannot have same color

## Recursive Approach

```
class Solution:
    def paintHouse(self, costs: list[list[int]]):
        n = len(costs)

        colors = {
            0: (1, 2),
            1: (0, 2),
            2: (0, 1)
        }

        dp = {}

        def dfs(h, col):
            if h >= n:
                return 0
            
            minCost = float('inf')

            for c in col:
                minCost = min(minCost, costs[h][c] + dfs(h + 1, colors[c]))
            
            return minCost 

        return dfs(0, (0, 1, 2))

costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19],
]

res = Solution().paintHouse(costs)
print(res)
```

## Memoization - Top_Down

```
class Solution:
    def paintHouse(self, costs: list[list[int]]):
        n = len(costs)

        colors = {
            0: (1, 2),
            1: (0, 2),
            2: (0, 1)
        }

        dp = {}

        def dfs(h, col):
            if h >= n:
                return 0
            
            if (h, col) in dp:
                return dp[(h, col)]
            
            minCost = float('inf')

            for c in col:
                minCost = min(minCost, costs[h][c] + dfs(h + 1, colors[c]))
            
            dp[(h, col)] = minCost

            return dp[(h, col)]  

        return dfs(0, (0, 1, 2))

costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19],
]

res = Solution().paintHouse(costs)
print(res)
```

## Tabulation - Bottom up

```

```