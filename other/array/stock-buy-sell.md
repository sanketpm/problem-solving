## Links
[Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

## Expected Output
Maximum Profit

## Approach

### Brute Force
1. min[] array -> recorded from left to right
2. max[] array -> recorded from right to left
3. From i--->n, calculate Max(max[i] - min[i])

```
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] max = new int[n];
        int[] min = new int[n];

        min[0] = prices[0];
        for(int i = 1; i < n; i++) {
            min[i] = Math.min(prices[i], min[i-1]);
        }
        
        max[n - 1] = prices[n - 1];
        for(int i = n - 2; i >= 0; i--) {
            max[i] = Math.max(prices[i], max[i + 1]);
        }

        int res = 0;
        for(int i = 0; i < n; i++) {
            res = Math.max(res, max[i] - min[i]);
        }

        return res;
    }
}
```

### Optimized
**Two pointers**
- `left` - buying price
- `right` - selling price
1. if prices[right] < prices[left] : move `left` to `right` 
2. if prices[left] >= prices[left]: 
   1. calculate current-profit & update max-profit
3. update right

```
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int left = 0;
        int right = 1;
        int maxProfit = 0;

        while(right < n) {
            if(prices[right] < prices[left]) {
                left = right;
            } else {
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            }
            ++right;
        }

        return maxProfit;
    }
}
```
**Questions**
1. Why are updating the left pointer to direct to right(`line 60`) instead of incrementing it one by one
   1. left only gets update when right dips below it
++left will only result incorrect result.

**Time Complexity**:
O(N)

**Space complexity**
O(1)