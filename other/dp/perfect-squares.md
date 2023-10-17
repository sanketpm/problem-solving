## links
[leetcode](https://leetcode.com/problems/perfect-squares/description/)

## Expected Output


## Recursive Approach

```
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        
        res = n

        i = 0
        while i*i <= n:
            i += 1
            square = i * i
            res = min(res, 1 + dfs(sum - square))
        
        return res
        
```

## Memoization - Top_Down

```
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def dfs(sum):
            if sum == 0:
                return 0
            
            if sum < 0:
                return n
            
            if dp[sum] != -1:
                return dp[sum]

            minSq = n

            i = 0
            while i*i <= n:
                i += 1
                minSq = min(minSq, 1 + dfs(sum - (i * i)))
           
            dp[sum] = minSq

            return minSq
        
        return dfs(n)
```

## Tabulation - Bottom up

```
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)

        dp[0] = 0

        for i in range(1, n + 1):

            j = 1
            while j * j <= i:
                square = j * j
                dp[i] = min(dp[i], 1 + dp[i - square])
                j += 1
        
        return dp[n]
```

**Editorial:**
1. https://leetcode.com/problems/perfect-squares/solutions/540782/the-question-is-coin-problem-in-disguise/
2. https://leetcode.com/problems/perfect-squares/solutions/3236383/279-solution-with-step-by-step-explanation/
