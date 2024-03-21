## links
[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/)

## Expected Output
Maximum Profit

**Constraints**:
1. You cannot `buy` unless you sell your bought stock
    - buy -> sell -> allowed
    - buy -> buy -> not allowed
    - sell -> sell -> not allowed
2. You can conduct only `two` transactions.
3. One Transaction = `buy` -> `sell`

> This problem is an extension of `Buy & Sell Stock II`
## Recursive Approach

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i, canBuy, limit):
            if i == n or limit == 0:
                return 0
            
            profit = 0

            if canBuy:
                buy = -prices[i] + dfs(i + 1, False, limit)
                dntBuy = dfs(i + 1, True, limit)
                profit = max(buy, dntBuy)
            else:
                sell = prices[i] + dfs(i + 1, True, limit - 1)
                dntSell = dfs(i + 1, False, limit)
                profit = max(sell, dntSell)
            
            return profit
        
        return dfs(0, True, 2)
```

## Memoization - Top_Down

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = {}

        def dfs(i, canBuy, limit):
            if i == n or limit == 0:
                return 0
            
            if (i, canBuy, limit) in dp:
                return dp[(i, canBuy, limit)]

            profit = 0

            if canBuy:
                buy = -prices[i] + dfs(i + 1, False, limit)
                dntBuy = dfs(i + 1, True, limit)
                profit = max(buy, dntBuy)
            else:
                sell = prices[i] + dfs(i + 1, True, limit - 1)
                dntSell = dfs(i + 1, False, limit)
                profit = max(sell, dntSell)
            
            dp[(i, canBuy, limit)] = profit

            return dp[(i, canBuy, limit)]
        
        return dfs(0, True, 2)
```

## Tabulation - Bottom up

```

```