## links
[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)

## Expected Output
Maximum Profit

**Constrainsts:
1. You cannot `buy` unless you sell your bought stock
    - buy -> sell -> allowed
    - buy -> buy -> not allowed
    - sell -> sell -> not allowed
2. You can conduct infinite transactions.

## Recursive Approach

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i, canBuy):
            if i == n:
                return 0

            profit = 0

            if canBuy:
                buy = -prices[i] + dfs(i + 1, False)
                dntBuy = dfs(i + 1, True)
                profit = max(buy, dntBuy)
            else:
                sell = prices[i] + dfs(i + 1, True)
                dntSell = dfs(i + 1, False)
                profit = max(sell, dntSell)
            
            return profit
        
        return dfs(0, True)
```

## Memoization - Top_Down

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = {}

        def dfs(i, canBuy):
            if i == n:
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            profit = 0

            if canBuy:
                buy = -prices[i] + dfs(i + 1, False)
                dntBuy = dfs(i + 1, True)
                profit = max(buy, dntBuy)
            else:
                sell = prices[i] + dfs(i + 1, True)
                dntSell = dfs(i + 1, False)
                profit = max(sell, dntSell)
            
            dp[(i, canBuy)] = profit

            return dp[(i, canBuy)]
        
        return dfs(0, True)
```

## Tabulation - Bottom up

```

```

**Questions**:
1. Why in `buy` have ` - prices[i] ` & in `sell` we have ` + prices[i] `
    - initial money = 0, profit & loss are based on this money (0), when you buy your money decreases, when you sell your money increases
    - buy: 1, sell: 7 => money = 6
2.  