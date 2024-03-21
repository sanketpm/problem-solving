## links
[leetcode](https://leetcode.com/problems/coin-change-ii/)

## Expected Output
Maximum no of way to ma

**Dry run:**
```
Input: amount = 5, coins = [1,2,5]
Output: 4

Explanation: there are four ways to make up the amount:

5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

## Recursive Approach

```

```

## Memoization Approach

```
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}

        def dfs(start, amt):
            if start == n or amt < 0:
                return 0
            
            if (start, amt) in dp:
                return dp[(start, amt)]
            
            if amt == 0:
                return 1
            
            ways = 0

            for i in range(start, n):
                ways += dfs(i, amt - coins[i])
            
            dp[(start, amt)] = ways
            return dp[(start, amt)]
            
        return dfs(0, amount)

```
## DP Approach

```
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(1, amount + 1):
                if c <= a:
                    dp[a] += dp[a - c]
        
        return dp[amount]
```