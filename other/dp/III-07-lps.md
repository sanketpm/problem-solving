## Links
[Leetcode](https://leetcode.com/problems/longest-palindromic-subsequence/)
[GFG](https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1)
[Other]()

## Expected Output
Length of the Longest Palindromic Subsequence

## Approach
1. Modified LCS
2. String1 remains same
3. String2 is reverse of String1
4. Return the LCS

**Tabulation - Bottom Up**
```
class Solution {
    public int longestPalinSubseq(String str) {
        int n = str.length();
        
        String rev = (new StringBuilder(str)).reverse().toString();
        
        int[][] dp = new int[n + 1][n + 1];
        
        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                if( str.charAt(i - 1) == rev.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[n][n];
    }
}
```