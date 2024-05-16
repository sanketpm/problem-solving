class Solution:
    def minCoins(self, coins: list[int], amount: int, N: int, dp: list[list[int]]) -> int:
        if N <= 0 or amount < 0:
            dp[N][amount] = 0
            return dp[N][amount]
        
        if amount == 0:
            dp[N][amount] = 0
            return 1
    

        pick = self.minCoins(coins, amount - coins[N - 1], N, dp)
        dontPick = self.minCoins(coins, amount, N - 1, dp)

        dp[N][amount] = pick + dontPick

        return pick + dontPick

    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [ [ -1 for i in range(amount + 1)] for j in range(n + 1)]
        
        for i in range(0, amount + 1):
            dp[0][i] = 0

        self.minCoins(coins, amount, n, dp)
        print(dp)
        return dp[n][amount]

res = Solution().coinChange([1, 2, 5], 11)
print(res)