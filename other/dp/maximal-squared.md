## links
[leetcode](https://leetcode.com/problems/maximal-square/description/)

## Expected Output

## Dry Run

Example 1:
```
1 1 1 1
1 1 1 1
0 1 1 1

```

Example 2:
```
1 0 1 1
1 1 0 1
1 1 1 1

```

Example 3:
```
1 0 1
0 1 1
0 1 1
```


- Cache is necessary to derive the solution
- Learn how the cache gets filled & you'll arrive the solution in top-down manner

## Memoization - Top_Down

```
class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        m, n = len(mat), len(mat[0])

        dp = {}

        def helper(r, c):
            if r >= m or c >= n:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            down = helper(r + 1, c)
            right = helper(r, c + 1)
            diag = helper(r + 1, c + 1)

            dp[(r, c)] = 0

            if mat[r][c] == '1':
                dp[(r, c)] = 1 + min(down, right, diag)

            return dp[(r, c)] # mat[r][c] -> 0
        
        helper(0, 0)
        
        maxArea = max( dp.values() ) ** 2

        return maxArea
```

## Tabulation - Bottom up

```

```


**Problems**
1. What is condition doing? 
```
if mat[r][c] == '1':
    dp[(r, c)] = 1 + min(down, right, diag)
```

2. Explain the helper function?
