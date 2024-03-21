## Links
[Leetcode](https://leetcode.com/problems/coin-change/description/)

## Expected Output
Min coins to make up to the given amount.
- Infinite number of coins

**Dry Run**
```
nums = [1, 2, 5]
amount = 11

op = 3

------------ 

nums = [1, 4, 2]
amount = 3

op = 2
```

## Recursive Approach

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def helper(start, amt):
            if amt == 0:
                return 0
            
            if amt < 0:
                return float('inf')
            
            min_coins = float('inf')

            for i in range(start, n):
                no_of_coins = 1 + helper(i, amt - coins[i])
                min_coins = min(min_coins, no_of_coins)
            
            return min_coins
        res = helper(0, amount) 

        return -1 if res == float('inf') else res
```

## Memoization Approach

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {}

        def helper(start, amt):
            if amt == 0:
                return 0
            
            if amt < 0:
                return float('inf')
            
            if (start, amt) in dp:
                return dp[(start, amt)]
            
            min_coins = float('inf')

            for i in range(start, n):
                no_of_coins = 1 + helper(i, amt - coins[i])
                min_coins = min(min_coins, no_of_coins)
            
            dp[(start, amt)] = min_coins
            return dp[(start, amt)]

        res = helper(0, amount) 

        return -1 if res == float('inf') else res
```

## DP Approach

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)

        for a in range(1, amount + 1):
            min_coins = float('inf')
            for c in range(n):
                if coins[c] <= a:
                    min_coins = min(min_coins, 1 + dp[a - coins[c]])
            dp[a] = min_coins
        
        return -1 if dp[amount] == float('inf') else dp[amount]
```