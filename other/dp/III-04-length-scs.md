## Links
[GFG](https://practice.geeksforgeeks.org/problems/shortest-common-supersequence0322/1)

## Expected Output
Length of shortest common supersequence

## Approach
1. Get the LCS length
2. Return str1_len + str2_len - lcs_len

**Approach - Tabulation**
```
class Solution
{
    
    public static int shortestCommonSupersequence(String X,String Y,int m,int n)
    {
        int[][] dp = new int[m + 1][n + 1];
        
        for(int i = 1; i < m + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                if( X.charAt(i - 1) == Y.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        int lcs = dp[m][n];
        
        return m + n - lcs;
    }
}
```