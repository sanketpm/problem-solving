class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for amt in range(1, amount):
            minCoins = float('inf') 
            for c in coins:
                if c > amt:
                    continue
                minCoins = min(minCoins, 1 + dp[amt - c])
            dp[amt] = minCoins
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
    
res = Solution().coinChange([2, 3, 5, 7], 7)

print(res)