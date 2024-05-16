class Solution:
    def coinSum(self, idx, coins, N, sum, dp):
        if sum < 0 or idx == N:
            return 0
        
        if sum == 0:
            return 1
        
        if dp[sum] != -1:
            return dp[sum]
        
        ways = 0
        
        for i in range(idx, N):
            ways += self.coinSum(i, coins, N, sum - coins[i], dp)
        
        dp[sum] = ways
        
        return dp[sum]
    
    def count(self, coins, N, Sum):
        dp = [-1] * (Sum + 1)
        return self.coinSum(0, coins, N, Sum, dp)

res = Solution().count([1, 2, 3], 3, 4)
print(res)