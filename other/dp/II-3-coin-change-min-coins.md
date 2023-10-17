## Links

## links
[leetcode](https://leetcode.com/problems/coin-change/)
[GFG](https://practice.geeksforgeeks.org/problems/number-of-coins1824/1)

## Expected Output
Min number of coins to make up the given `amount`

e.g.:
**Input:**
coins = [1, 2, 5]
amount = 11

**Output:**
- 3
-> [5, 5, 1]

## Recursive Approach

## Optimized Approach

**Recursive**
```
class Solution{
	public int minCoins(int coins[], int N, int sum) {
        if( sum == 0 ) {
	        return 0;
	    }

	    if( N == 0 ) {
	        return Integer.MAX_VALUE - 1;
	    }

	    if( coins[N-1] <= sum ) {
	        return Math.min( 
    	                1 + mincoins(coins, N, sum - coins[N-1]), 
    	                mincoins(coins, N - 1, sum) 
	               );
	    } else {
	        return mincoins(coins, N - 1, sum);
	    }
	} 
}
```

**Memoized Approach**
```
class Solution{
    private int mincoins(int coins[], int N, int sum, int[][] dp) {
	    if( sum == 0 ) {
	        return 0;
	    }

	    if( N == 0 ) {
	        return Integer.MAX_VALUE - 1;
	    }

	    if( dp[N][sum] != -1 ) {
	        return dp[N][sum];
	    }

	    if( coins[N-1] <= sum ) {
	        return dp[N][sum] = Math.min( 
    	                1 + mincoins(coins, N, sum - coins[N-1], dp), 
    	                mincoins(coins, N - 1, sum, dp) 
	               );
	    } else {
	        return dp[N][sum] = mincoins(coins, N - 1, sum, dp);
	    }
    }

	public int minCoins(int coins[], int N, int sum) {
	    int[][] dp = new int[N + 1][sum + 1];

	    for( int[] arr : dp ) {
	        Arrays.fill(arr, -1);
	    }

	    mincoins(coins, N, sum, dp);

        return dp[N][sum] == Integer.MAX_VALUE-1?-1: dp[N][sum];
	} 
}
```

**Tabulation Approach**
```
class Solution{
	public int minCoins(int coins[], int N, int sum) {
	    
	    int[][] dp = new int[N + 1][sum + 1];
	    
	    for( int[] arr : dp ) {
	        Arrays.fill(arr, -1);
	    }
	    
	    for(int i = 0; i < sum + 1; i++) {
	        dp[0][i] = Integer.MAX_VALUE - 1;
	    }
	    
	    for(int i = 0; i < N + 1; i++) {
	        dp[i][0] = 0;
	    }
	    
	    for(int i = 1; i < N + 1; i++) {
	        for(int j = 1; j < sum + 1; j++) {
	            if( coins[i - 1] <= j) {
	                dp[i][j] = Math.min( 1 + dp[i][j - coins[i-1]], dp[i-1][j]);
	            } else {
	                dp[i][j] = dp[i-1][j];
	            }
	        }
	    }

        return dp[N][sum] == Integer.MAX_VALUE-1?-1: dp[N][sum];
	} 
}
```


## Python

![image](./II-3-coin-change-min-coins.md)

**Recursive**

```
class Solution:
    def minCoins(self, n: int, coins: List[int], amount: int) -> int:
        if amount < 0:
            return (10 ** 4) + 1 
        
        if amount == 0:
            return 0

        minCoin = (10 ** 4)

        for i in range(n):
            minCoin = min(minCoin, 1 + self.minCoins(n, coins, amount - coins[i]))
        
        return minCoin 

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        minCoin = self.minCoins(n, coins, amount)

        if minCoin == 10 ** 4:
            return -1
        
        return minCoin
```

**Memoization:**

```
class Solution:
    def minCoins(self, n: int, coins: List[int], amount: int, dp: List[List[int]]) -> float:
        if amount < 0:
            return float('inf')
        
        if amount == 0:
            return 0
        
        if dp[amount] != -1:
            return dp[amount]

        minCoin = float('inf')

        for i in range(n):
            minCoin = min(minCoin, 1 + self.minCoins(n, coins, amount - coins[i], dp))
        
        dp[amount] = minCoin
        
        return dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1] * (amount + 1)

        minCoin = self.minCoins(n, coins, amount, dp)

        if minCoin == float('inf'):
            return -1
        
        return minCoin
```

**Dynamic Programming**

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for amt in range(1, amount + 1):
            minCoins = float('inf') 
            for c in coins:
                if c > amt:
                    continue
                minCoins = min(minCoins, 1 + dp[amt - c])
            dp[amt] = minCoins
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
```