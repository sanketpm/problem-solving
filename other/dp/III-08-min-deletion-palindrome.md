## Links
[GFG](https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions4610/1)

## Expected Output
Minimum Number of deletions to make a string into palindrome

## Approach
1. Find LPS (Longest Palindromic Subsequence)
2. `Length_of_string` - `Length_of_LPS` = `# of deletion` to make the string palindrome

**Tabulation - Bottom Up**
```
class Solution  { 
    
    int minDeletions(String str, int n) {
        String rev = new StringBuilder(str).reverse().toString();
        
        int[][] dp = new int[n + 1][n + 1];
        
        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                if( str.charAt(i - 1) == rev.charAt(j - 1) ) {
                    dp[i][j] = 1 + dp[i -1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return n - dp[n][n];
    }
}
```