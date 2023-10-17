## links
[leetcode](https://leetcode.com/problems/integer-break)

## Expected Output


## Recursive Approach

```
class Solution:
    def integerBreak(self, n: int) -> int:

        def dfs(n):
            if n < 2:
                return 0
            
            max_prod = 0

            for i in range(1, n):
                curr_max_prod = max(dfs(n - i), n - i)
                max_prod = max(max_prod, curr_max_prod * i)
            
            return max_prod

        return dfs(n)
```

## Memoization - Top_Down

```
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}    

        def dfs(n):
            if n < 2:
                return 0
            
            if n in dp:
                return dp[n]
            
            max_prod = 0

            for i in range(1, n):
                curr_max_prod = max(dfs(n - i), n - i)
                max_prod = max(max_prod, curr_max_prod * i)
            
            dp[n] = max_prod

            return dp[n]
            
        return dfs(n)
```

## Tabulation - Bottom up

```
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 0
        dp[2] = 1

        for num in range(1, n + 1):
            max_prod = 0

            for i in range(1, num):
                curr_max_prod = max(num - i, dp[num - i]) * i
                max_prod = max(max_prod, curr_max_prod)

            dp[num] = max_prod
        
        return dp[n]
```