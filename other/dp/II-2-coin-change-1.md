## Links
[GFG](https://practice.geeksforgeeks.org/problems/coin-change2448/1)

## Expected Output
Maximum Number of way the coins can make the sum.
- Infinite number of coins

## Recursive Approach

## Memoization - Top Down

## Tabulation - Bottom Up

**Recursive**
```
class Solution {
    public long count(int coins[], int N, int sum) {
       if( N == 0 ) {
           return 0;
       }
       
       if( sum == 0 ) {
           return 1;
       }
       
       if( coins[N - 1] <= sum ) {
           return count(coins, N, sum - coins[N - 1]) + count(coins, N - 1, sum);
       } else {
           return count(coins, N - 1, sum);
       }
    }
}
```

**Memoization - Top Down**
```
class Solution {
    
    private long count(int[] coins, int N, int sum, long[][] dp) {
        if( N == 0 ) {
            return 0;
        }
        
        if( sum == 0 ) {
            return 1;
        }
        
        if( dp[N][sum] != -1 ) {
            return dp[N][sum];
        }
        
        if( coins[N - 1] <= sum ) {
            return dp[N][sum] = count(coins, N, sum - coins[N - 1], dp) + count(coins, N - 1, sum, dp);
        } else {
            return dp[N][sum] = count(coins, N - 1, sum, dp);
        }
    }
    
    public long count(int coins[], int N, int sum) {
        long[][] dp = new long[N + 1][sum + 1];
        
        for(long[] arr: dp) {
            Arrays.fill(arr, -1);
        }
        
        return count(coins, N, sum, dp);
    }
}
```

**Tabulation - Bottom Up**
```
class Solution {
    
    public long count(int coins[], int N, int sum) {
        long[][] dp = new long[N + 1][sum + 1];
        
        for(int i = 0; i < sum + 1; i++) {
            dp[0][i] = 0;
        }
        
        for(int i = 0; i < N + 1; i++) {
            dp[i][0] = 1;
        }
        
        /**
         * N = i
         * sum = j
         **/
        for(int i = 1; i < N + 1; i++) {
            for(int j = 1; j < sum + 1; j++) {
                if(coins[i - 1] <= j) {
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[N][sum];
    }
}
```