## links
[leetcode](https://leetcode.com/problems/min-cost-climbing-stairs/description/)

## Expected output
Minimum cost to to reach the top

## Recursive approach
- Modified climbing stairs

**code**
```
class Solution:
    def minCost(self, n: int, cost: List[int]) -> int:
        if n < 0:
            return 0
        
        if n == 0 or n == 1:
            return cost[n]
        
        oneStep = self.minCost(n - 1, cost)
        twoStep = self.minCost(n - 2, cost)

        return cost[n] + min(oneStep, twoStep)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        oneStep = self.minCost(n - 1, cost)
        twoStep = self.minCost(n - 2, cost)

        return min(oneStep, twoStep)
```

## Memoization - top down


**code**
```
class Solution:
    def minCost(self, n: int, cost: List[int], dp: List[int]) -> int:
        if n < 0:
            return 0
        
        if n == 0 or n == 1:
            return cost[n]
        
        if dp[n] != 0:
            res = dp[n]
            return dp[n]
        
        oneStep = self.minCost(n - 1, cost, dp)
        twoStep = self.minCost(n - 2, cost, dp)

        dp[n] = cost[n] + min(oneStep, twoStep)
        res = dp[n]
        
        return res

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * n

        oneStep = self.minCost(n - 1, cost, dp)
        twoStep = self.minCost(n - 2, cost, dp)

        return min(oneStep, twoStep)
```

## Tabulation - bottom up

**code**
```
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * (n)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2]) 
```

**Pneumonic**
- If you can draw the recursive tree for this problem, then its done
- Memoization & Tabulation can be derived from recusion

**Mistakes**
1. I tought that `dfs` should only be called once, my fixed mindset allowed to me fail to come up with a solution,
2. Fixed minset effected Tabulation solution also
3. I did not focus much on the specifics when debugging

- Even if you've solved any problem before do not take it lightly, approach it with a fresh mindset - you can solve questions easily then else you will fail