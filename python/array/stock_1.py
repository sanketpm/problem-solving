class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 0
        maxprofit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            right+=1
        
        return maxprofit

result = Solution().maxProfit([7, 1, 5, 3, 6, 4])
print(result)
