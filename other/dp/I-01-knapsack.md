## Links
[GFG](https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)

## Expected Output
Maximum profit by selecting best possible weights

## Recursive Approach
1. Max( Select & recur , Dont select & recur)
2. Here,
   1. SELECT        : Reduce Knapsack capacity, Go previous Item
   2. NOT SELECTED  : Knapsack capacity doesnt change, Go previous Item

## Memoization - Top Down
1. Max values for recursion for N(No of items) & W(knapsack capacity) are the bounds for a recursion
2. We can create a 2D array representing each function call
   1. each cell of this array represents parameter value & value it returns

## Tabulation - Bottom Up
1. Model it after Memoization but bottom 

**Dry Run**
```
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7

op: 

```

**Recursive**
```
class Solution 
{ 
    //Function to return max value that can be put in knapsack of capacity W.
    static int knapSack(int W, int wt[], int val[], int n) 
    { 
         if( W == 0 || n == 0 ) {
             return 0;
         }
         
         if( wt[n - 1] <= W ) {
             return Math.max(
                val[n -1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                knapSack(W, wt, val, n - 1)
             );
         } else {
             return knapSack(W, wt, val, n - 1);
         }
    } 
}
```

**Memoization - Top Down**
```
class Solution 
{ 
    static int knapsack(int W, int[] wt, int[] val, int n, int[][] dp) {
        if( W == 0 || n == 0 ) {
             return 0;
        }
        
        if( dp[n][W] != -1 ) {
            return dp[n][W];
        }
                 
        if( wt[n - 1] <= W ) {
            return dp[n][W] = Math.max(
                val[n -1] + knapsack(W - wt[n - 1], wt, val, n - 1, dp),
                knapsack(W, wt, val, n - 1, dp)
            );
        } else {
            return dp[n][W] = knapsack(W, wt, val, n - 1, dp);
        }
    }
    
    //Function to return max value that can be put in knapsack of capacity W.
    static int knapSack(int W, int wt[], int val[], int n) 
    { 
        int[][] dp = new int[n + 1][W + 1];
        
        for(int[] arr: dp) {
            Arrays.fill(arr, -1);
        }
        
        knapsack(W, wt, val, n, dp);
        
        return dp[n][W];
    } 
}
```

**Tabulation - Bottom Up**
```
class Solution 
{ 
    //Function to return max value that can be put in knapsack of capacity W.
    static int knapSack(int W, int wt[], int val[], int n) 
    { 
        int[][] dp = new int[n + 1][W + 1];
        
        for(int i = 0; i < W + 1; i++) {
            dp[0][i] = 0;
        }
        
        for(int i = 0; i < n + 1; i++) {
            dp[i][0] = 0;
        }
        
        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < W + 1; j++) {
                if(wt[i -1] <= j) {
                    dp[i][j] = Math.max( val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j] );
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[n][W];
    } 
}
```

## Python

**Brute Force**
```
class Solution:
    def knapSack(self,W, wt, val, n):
        def helper(n, W):
            if W == 0 or n == 0:
                return 0
            
            pick, dntPick = 0, 0
            
            if wt[n - 1] <= W:
                pick = val[n - 1] + helper(n - 1, W - wt[n - 1])

            dntPick = helper(n - 1, W)
            
            return max(pick, dntPick)
        
        return helper(n, W)
```

**Memorization**
```
class Solution:
    def knapSack(self,W, wt, val, n):
        dp = [ [-1] * (W + 1) for _ in range(n + 1)]
        
        def helper(n, W):
            if W == 0 or n == 0:
                return 0
            
            if dp[n][W] != -1:
                return dp[n][W]
            
            pick, dntPick = 0, 0
            
            if wt[n - 1] <= W:
                pick = val[n - 1] + helper(n - 1, W - wt[n - 1])

            dntPick = helper(n - 1, W)
            
            dp[n][W] = max(pick, dntPick)
            
            return dp[n][W]

        return helper(n, W)
```

**DP**

```
class Solution:
    def knapSack(self,W, wt, val, n):
        dp = [ [0] * (W + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                pick, dntPick = 0, 0
                if wt[i - 1] <= j:
                    pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                
                dntPick = dp[i - 1][j]
                dp[i][j] = max(pick, dntPick)

        return dp[n][W]
```

**Learnings**
1. Keep the other function names very distinct to avoid compilation errors
2. Model you DP solution with Memoization on the side, do not attempt to write the DP without Memoization to compare & infer