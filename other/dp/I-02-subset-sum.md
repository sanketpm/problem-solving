## Links
[GFG](https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1)

## Expected Output
Return true/false: Whether any subset which produces the sum exist

**Dry run**
```
arr = [2, 3, 7, 8, 10]
sum = 11
op: True


```

## Recursive Approach
- `take` & `dntTake` pattern of recursion

**Recursive**
```
class Solution{
    static Boolean isSubsetSum(int N, int arr[], int sum){
        if(sum == 0) {
            return true;
        }

        if( N == 0 ) {
            return false;
        }
                
        // element > sum : ignore it
        if(arr[N-1] > sum) {
            return isSubsetSum(N-1, arr, sum);
        } else {
        // element <= sum: choose it / skip it
            return isSubsetSum(N-1, arr, sum-arr[N-1]) || isSubsetSum(N-1, arr, sum);
        }
    }
}
```

**Memoization - Top Down**
```
class Solution{
    static int subsetSum(int N, int[] arr, int sum, int[][] dp) {
        if( sum == 0 ) {
            return 1;
        }
        
        if( N == 0 ) {
            return 0;
        }
        
        if( dp[N][sum] != -1 ) {
            return dp[N][sum];
        }
        
        if( arr[N - 1] > sum ) {
            return dp[N][sum] = subsetSum(N - 1, arr, sum, dp);
        } else {
            return dp[N][sum] = subsetSum(N - 1, arr, sum - arr[N -1], dp) | subsetSum(N - 1, arr, sum, dp);
        }
    }
    
    static Boolean isSubsetSum(int N, int arr[], int sum){
        int[][] dp = new int[N + 1][sum + 1];
        
        for( int[] temp : dp ) {
            Arrays.fill(temp, -1);
        }
        
        subsetSum(N, arr, sum, dp);
        
        return dp[N][sum] == 1;
    }
}
```

**Tabulation - Bottom Up**
```
class Solution{
    static Boolean isSubsetSum(int N, int arr[], int sum){
        boolean[][] dp = new boolean[N + 1][sum + 1];
        
        for(int i = 0; i < N + 1; i++) {
            dp[i][0] = true;
        }
        
        for(int i = 1; i < N + 1; i++) {
            for(int j = 1; j < sum + 1; j++) {
                if(arr[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[N][sum];
    }
}
```

## Python

**Recursion**

```
class Solution:
    def isSubsetSum (self, N, arr, sum):
        if N == 0 or sum < 0:
            return False
        
        if sum == 0:
            return True
        
        take = self.isSubsetSum(N - 1, arr, sum - arr[N - 1])
        dntTake = self.isSubsetSum(N - 1, arr, sum)
        
        return take or dntTake
```

**Memoization**:

```
    def isSubsetSum (self, N, arr, sum):
        dp = [ [-1] * (sum + 1) for _ in range(N + 1)]

        def dfs(i, sum):
            if sum == 0:
                return True
            
            if i == N or sum < 0:
                return False
            
            if dp[i][sum] != -1:
                return dp[i][sum]
            
            pick, dntPick = 0, 0
            
            if arr[i] <= sum:
                pick = dfs(i + 1, sum - arr[i])
            
            dntPick = dfs(i + 1, sum)

            dp[i][sum] = pick | dntPick

            return dp[i][sum]
        
        return True if dfs(0, sum) == 1 else False
```

**Tabulation**
```
class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp = [[False] * (sum + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            dp[i][0] = True
        
        for i in range(1, N + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[N][sum]
```

**Where I missed the edge case**
### 1: Incorrect base condition
**I did:**
```
class Solution:
    def subSetSum(self, N, arr, sum, dp):
        if N == 0 or sum < 0:
            return 0
        
        if sum == 0:
            return 1
```

**Correct**
```
class Solution:
    def subSetSum(self, N, arr, sum, dp):
        if sum == 0:
            return 1
        
        if N == 0 or sum < 0:
            return 0
```

The first base condition fails when you have a subset where all elements of the array form the sum.

Here, instead of hitting the condition `sum == 0 -> True` we hit `N == 0 -> False`, \
Therefore, toggle them
1. Check if `sum == 0` only after this
2. Check `N == 0` or `sum < 0`

### 2: why is dp[row][0] initialized to True
```
for i in range(N + 1):
    dp[i][0] = True
```


