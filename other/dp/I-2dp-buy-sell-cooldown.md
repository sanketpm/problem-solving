## links
[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

## Expected output


## Memoization approach

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def dfs(i, buying):
            if i >= n:
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = -prices[i] + dfs(i + 1, not buying) 
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                '''
                - After selling, you skip next next day 
                - that's why its `i + 2`, instead of `i + 1
                '''
                sell = prices[i] + dfs(i + 2, not buying)
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return dfs(0, True)
```