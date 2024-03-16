## Links
[GFG](https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1)

## Expected Output
Minimum number of partitions to the given string, where all partitioned strings are palindromes

## Recursive Approach

## Memoization - Top Down

## Tabulation - Bottom Up

**Recursive**
```
class Solution{
    private static boolean isPalindrome(String str, int i, int j) {
        while(i < j) {
            if( str.charAt(i) != str.charAt(j) ) {
                return false;
            }
            ++i;
            --j;
        }
        
        return true;
    }
    
    private static int partition(String str, int i, int j) {
        if( i >= j ) {
            return 0;
        }
        
        if( isPalindrome(str, i, j) ) {
            return 0;
        }
        
        int minPartition = Integer.MAX_VALUE;
        
        for(int k = i; k <= j - 1; k++ ) {
            int res = 1 + partition(str, i , k) + partition(str, k + 1, j);
            minPartition = Math.min(minPartition, res);
        }
        
        return minPartition;
    }
    
    static int palindromicPartition(String str)
    {
        return partition(str, 0, str.length() - 1);
    }
}
```

**Memoization - Top Down**
```
class Solution{
    private static boolean isPalindrome(String str, int i, int j) {
        while(i < j) {
            if( str.charAt(i) != str.charAt(j) ) {
                return false;
            }
            ++i;
            --j;
        }
        
        return true;
    }
    
    private static int partition(String str, int i, int j, int[][] dp) {
        if( i >= j ) {
            return dp[i][j] = 0;
        }
        
        if( isPalindrome(str, i, j) ) {
            return dp[i][j] = 0;
        }
        
        if( dp[i][j] != -1 ) {
            return dp[i][j];
        }
        
        int minPartition = Integer.MAX_VALUE;
        
        for(int k = i; k <= j - 1; k++ ) {
            int res = 1 + partition(str, i , k, dp) + partition(str, k + 1, j, dp);
            minPartition = Math.min(minPartition, res);
        }
        
        return dp[i][j] = minPartition;
    }
    
    static int palindromicPartition(String str)
    {
        int n = str.length();
        
        int[][] dp = new int[n][n];
        
        for(int[] t: dp) {
            Arrays.fill(t, -1);
        }
        
        return partition(str, 0, str.length() - 1, dp);
    }
}
```

**Tabulation - Bottom Up**
```
class Solution{
    static boolean isPalindrome(String str, int i, int j) {
        while( i <= j ) {
            if( str.charAt(i) != str.charAt(j) ) {
                return false;
            }
            ++i;
            --j;
        }
        return true;
    }
    
    static int palindromicPartition(String str) {
        int n = str.length();
        int[][] dp = new int[n][n];
        
        for(int i = n - 1; i >= 0; i--) {
            for(int j = i; j < n; j++) {
                
                
                if( i == j || isPalindrome(str, i, j)) {
                    dp[i][j] = 0;
                    continue;
                }
                
                int minPartition = Integer.MAX_VALUE;
                
                for(int k = i; k <= j - 1; k++) {
                    int ops = 1 + dp[i][k] + dp[k + 1][j];
                    minPartition = Math.min(minPartition, ops);
                }
                dp[i][j] = minPartition;
            }
        }
        
        return dp[0][n - 1];
    }
}
```